# Telegram Custom Emoji Mapper

This tool helps to download custom emojis from Telegram packs and map them to names for further use. It consists of two main components:

1.  **A Telegram Bot (`bot.py`)**: To download `.webp` files from any public sticker pack
2.  **A Mapper GUI (`mapper_gui.py`)**: A script that generates a local HTML interface for you to visually assign names to the downloaded emojis and export the result as a `JSON` file

## Setup

1.  **Clone the Repository**

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create Environment File**
    ```bash
    cp .env.example .env
    ```

4.  **Configure Your Credentials**
    Open the `.env` file and fill in your Telegram API credentials and Bot Token. You can get your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org)
    ```env
    # .env
    API_ID=12345678
    API_HASH="your_api_hash_here"
    BOT_TOKEN="your_bot_token_here"
    ```

### Step 1: Download Emojis with the Bot

1.  **Run the bot script**
    ```bash
    python emojimapper/bot.py
    ```

2.  **Find your bot in Telegram** and send it the `/scan` command with the short name of the sticker pack you want to download
    ```
    /scan YourPackShortname
    ```

3.  The bot will download all custom `.webp` emojis from that pack into a folder inside `download/` (`download/YourPackShortname/`) by default

### Step 2: Map Emojis with the GUI

1.  **Run the GUI generator script:**
    ```bash
    python emojimapper/mapper_gui.py
    ```

2.  **Select the pack:** The script will show a list of downloaded packs. Enter the name of the folder you just created (`YourPackShortname`)

3.  **Open the HTML file:** A file named `emoji_mapper.html` will be created in the project root. Open it in any web browser

4.  **Assign names:** In the browser, type a name for each emoji that you need in the input field next to it (you can skip some of if you want)

5.  **Save the results:** Click the "Save JSON" button at the bottom. Your browser will download a file named `mapped_emoji.json`, which contains your final mappings

## Output File

The final `mapped_emoji.json` will look like this:

```json
{
  "5304268384992906817": "YourEnteredName1",
  "5304268384992906818": "YourEnteredName2",
  "5304268384992906819": "YourEnteredName3"
}
```