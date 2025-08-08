import asyncio

def main():
    """Main menu to select the operating mode."""
    choice = input(
        "Select what to run:\n"
        "1. Telegram bot to download emojis (/scan)\n"
        "2. GUI to map emojis to names\n"
        "Enter a number (1-2): "
    ).strip()

    if choice == "1":
        from bot import main_bot
        asyncio.run(main_bot())
    elif choice == "2":
        from mapper_gui import create_mapper_gui
        create_mapper_gui()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()