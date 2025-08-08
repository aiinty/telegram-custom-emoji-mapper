import os
import json
from jinja2 import Environment, FileSystemLoader
from config import DOWNLOAD_DIR

OUTPUT_HTML_FILENAME = "emoji_mapper.html"
TEMPLATES_DIR = "templates"

def get_pack_folder_path():
    print(f"Emoji pack folders should be located in: '{DOWNLOAD_DIR}'")
    
    try:
        if not os.path.exists(DOWNLOAD_DIR) or not os.path.isdir(DOWNLOAD_DIR):
             print(f"⚠️ Warning: The directory '{DOWNLOAD_DIR}' doesn't exist")
             return None

        subdirectories = [d for d in os.listdir(DOWNLOAD_DIR) if os.path.isdir(os.path.join(DOWNLOAD_DIR, d))]
        
        if subdirectories:
            print("\nAvailable packs found:")
            for i, pack_name in enumerate(subdirectories, 1):
                print(f"  {i}. {pack_name}")
        else:
            print("\nNo packs found")
    except Exception as e:
        print(f"An error occurred while finding packs: {e}")
    
    pack_name = input("👉 Enter the name of the pack folder to process: ").strip()

    if not pack_name:
        print("❌ No folder name entered")
        return None

    folder_path = os.path.join(DOWNLOAD_DIR, pack_name)
    if not os.path.isdir(folder_path):
        print(f"❌ Error: Folder '{folder_path}' does not exist")
        return None
    return folder_path

def parse_emoji_files(folder_path):
    webp_files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith(".webp")],
        key=lambda name: int(name.split("_")[0])
    )
    if not webp_files:
        print(f"🤷 No .webp found in '{folder_path}'")
        return []

    items = []
    for filename in webp_files:
        try:
            parts = filename.split("_")
            items.append({
                "emoji_char": parts[1],
                "emoji_id": parts[2].split(".")[0],
                "file_path": os.path.join(folder_path, filename).replace('\\', '/'),
            })
        except IndexError:
            print(f"⚠️ Skipping file with incorrect name format: {filename}")
    return items

def create_mapper_gui():
    folder_path = get_pack_folder_path()
    if not folder_path:
        return

    emoji_items = parse_emoji_files(folder_path)
    if not emoji_items:
        return

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("mapper_template.html")

    html_content = template.render(items=emoji_items)

    try:
        with open(OUTPUT_HTML_FILENAME, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"\n✅ Done! Open '{OUTPUT_HTML_FILENAME}' in your browser")
    except IOError as e:
        print(f"❌ Error writing: {e}")

if __name__ == "__main__":
    create_mapper_gui()