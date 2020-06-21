import requests
import random
from podcast_bot import TalkPythonBot
from greetings import greetings

# Create the bot object to interact with the Telegram API
bot = TalkPythonBot()


def make_reply(msg, name):
    """
    This function generates the messages that are sent to the user for the '/start' command and the default message in case the Talk Python search api does not return a result.

    Parameters
    ----------
    msg : string
        The command / message entered by the user in Telegram
    name : string
        The name of the Telegram user

    Returns
    -------
    string
        The message displayed to the Telegram user
    """
    results = None
    name = name if name else "there"

    results = (
        f"{random.choice(greetings)}, {name}! 👋 \n\nSearch for <a href='https://talkpython.fm'>TalkPython</a> episodes based on a topic (example, <strong>flask</strong>). To search with multiple words, separate them with a '-' (example, <strong>flask-mongo</strong>)"
        if msg == "/start"
        else get_results(msg)
    )

    if len(results) == 0:
        results = f"Sorry! I did not find anything for <strong><em>{msg}</em></strong> 😟"

    return results


def get_results(msg):
    """
    Returns the final message containing the list of episodes returned by the Talk Python api based on the search text entered in Telegram

    Parameters
    ----------
    msg : string
        The search text entered by the user in Telegram

    Returns
    -------
    string
        The list of all the episodes returned by the Talk Python search api
    """

    message_body_list = []
    message_body = ""
    message_heading = f"🐍🤩 Popular <strong><a href='https://talkpython.fm'>Talk Python To Me</a></strong> episodes for <strong><em>{msg}</em></strong>:\n"

    r = requests.get(f"https://search.talkpython.fm/api/search?q={msg}")

    # Limit to the 15 most popular episodes only
    search_results = r.json()["results"][:15]

    for result in search_results:
        if result["category"] == "Episode":
            message_body_list.append(
                f"\n\n👉 <strong>Episode {result['id']}</strong> 〰️ <a href='https://talkpython.fm{result['url']}'>{result['title']}</a>"
            )

    for item in message_body_list:
        item = item.replace("#", "")
        message_body += item

    if message_body:
        return message_heading + message_body
    else:
        return ""


def get_reply(item, KEY):
    """Depending on whether the Telegram JSON contains the 'message' or 'edited_message' keys, the function parses the JSON object and returns the final response to be displayed to the user

    Parameters
    ----------
    item : dictionary
        The Telegram dictionary object
    KEY : string
        Either 'message' or 'edited_message'

    Returns
    -------
    string
        The final message to be displayed to the Telegram user
    """

    name = item[KEY]["from"]["first_name"]
    message = str(item[KEY]["text"]).lower()
    message = message.replace("&", "-").replace("#", "-")
    return make_reply(message, name)


def main():
    """
    The function gets the reply to be sent to the telegram user and the chat id for the message instance and calls the send_message method of the Telegram API.
    """
    update_id = None
    from_user = None
    reply = None

    while True:
        print("Firing up the Talk Python bot...")
        updates = bot.get_updates(offset=update_id)
        updates = updates["result"]

        if updates:

            for item in updates:
                update_id = item["update_id"]

                # For edits, telegram changes the "message" key to "edited_message"
                if "message" in item.keys():
                    MSG_KEY = "message"
                    from_user = item[MSG_KEY]["from"]["id"]
                    reply = get_reply(item, MSG_KEY)
                elif "edited_message" in item.keys():
                    MSG_KEY = "edited_message"
                    from_user = item[MSG_KEY]["from"]["id"]
                    reply = get_reply(item, MSG_KEY)

                bot.send_message(reply, from_user)


if __name__ == "__main__":
    main()
