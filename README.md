# Talk Python Podcast - Telegram Bot

This repository contains the Python (v3.7) code for the [Talk Python Podcast Telegram bot](https://t.me/@TalkPythonBot).

## Using the bot

1. Search for the bot in Telegram using either **Talk Python Podcast** or **@TalkPythonBot**
2. Click **START** to begin conversing with the bot
3. To search for podcast episodes, send any search text (for example, `django`)
4. To search with multiple words, separate them with a `-` (for example, `flask-mongo`)

## Commands
1. `/start` - To start interacting with the bot and get a welcome message
2. Any search text

## Creating a local setup

1. Clone the current repository - `git clone https://github.com/Bots-Telegram/talk-python-bot`
2. Create a virtual environment - `python -m venv venv`
3. Activate the virtual environment - `venv\Sctipts\activate.bar` (Windows), `source venv/bin/activate` (OSx / Linux)
4. Install the project dependencies - `pip install -r requirements.txt`
5. Create a `.env` file and add an environment variable called `TELEGRAM_TOKEN` (refer to `.env.example`)
6. Run the code - `python bot/server.py` or `python3 bot/bot_server.py`
7. To run the tests - `pytest`

---

<p align="center"><img src="https://github.com/Bots-Telegram/talk-python-bot/blob/master/images/bot1.jpg" alt="Bot1"></p>

---

<p align="center"><img src="https://github.com/Bots-Telegram/talk-python-bot/blob/master/images/bot2.jpg" alt="Bot2"></p>
