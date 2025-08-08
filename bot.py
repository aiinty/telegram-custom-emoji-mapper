import os
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName, DocumentAttributeCustomEmoji
from config import API_ID, API_HASH, BOT_TOKEN, SESSION, DOWNLOAD_DIR

async def main_bot():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    
    @client.on(events.NewMessage(pattern=r'/scan (.+)'))
    async def scan_emoji_pack(event):
        # Get the short name from the user's message ("https://t.me/addemoji/ZZZchatsticks" is "/scan ZZZchatsticks")
        short_name = event.pattern_match.group(1)

        try:
            result = await client(GetStickerSetRequest(
                stickerset=InputStickerSetShortName(short_name=short_name),
                hash=0
            ))

            save_dir = os.path.join(DOWNLOAD_DIR, short_name)
            os.makedirs(save_dir, exist_ok=True)

            saved_files = []
            for i, doc in enumerate(result.documents):
                # Check if any of the attributes mark it as a custom emoji
                is_custom = any(isinstance(attr, DocumentAttributeCustomEmoji) for attr in doc.attributes)

                if is_custom:
                    emoji_char = "unknown"
                    # Extract the emoji character
                    for attr in doc.attributes:
                        if isinstance(attr, DocumentAttributeCustomEmoji):
                            emoji_char = attr.alt or "unknown"
                            break
                    
                    filename = f"{i:02d}_{emoji_char}_{doc.id}.webp"
                    path = os.path.join(save_dir, filename)
                    
                    await client.download_media(doc, file=path)
                    saved_files.append(filename)

            if not saved_files:
                await event.reply("❌ No custom emojis found.")
                return

            text = f"✅ Downloaded {len(saved_files)} emojis to <code>{save_dir}</code> folder\n\n"
            text += "\n".join(saved_files[:15])
            if len(saved_files) > 15:
                text += f"\n...and {len(saved_files) - 15} more"

            await event.reply(text, parse_mode="html")
            
        except Exception as e:
            await event.reply(f"⚠️ Error:\n<code>{e}</code>", parse_mode="html")

    print("🤖 Bot is starting...")
    await client.start(bot_token=BOT_TOKEN)

    print("✅ Bot is running. Send /scan <short_name> to scan a pack.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main_bot())