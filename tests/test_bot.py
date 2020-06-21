import os
import requests
import dotenv
import bot_server

dotenv.load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")


def test_telegram_get_updates(requests_mock):
    requests_mock.get(
        f"https://api.telegram.org/bot{token}/getUpdates", json={"kw": "flask"}
    )
    assert {"kw": "flask"} == requests.get(
        f"https://api.telegram.org/bot{token}/getUpdates"
    ).json()


def test_tp_search_api_single_word(requests_mock):
    requests_mock.get(
        "https://search.talkpython.fm/api/search?q=flask", json={"kw": "flask"}
    )
    assert {"kw": "flask"} == requests.get(
        "https://search.talkpython.fm/api/search?q=flask"
    ).json()


def test_tp_search_api_multi_word(requests_mock):
    requests_mock.get(
        "https://search.talkpython.fm/api/search?q=flask-mongo",
        json={"kw": "flask-mongo"},
    )
    assert {"kw": "flask-mongo"} == requests.get(
        "https://search.talkpython.fm/api/search?q=flask-mongo"
    ).json()


def test_tp_search_api_special_character(requests_mock):
    requests_mock.get(
        "https://search.talkpython.fm/api/search?q=flask%mongo*postgres",
        json={"kw": "flask-mongo-postgres"},
    )
    assert {"kw": "flask-mongo-postgres"} == requests.get(
        "https://search.talkpython.fm/api/search?q=flask%mongo*postgres"
    ).json()


def test_make_reply():
    result = bot_server.make_reply("bohemianraphsody!@@", "test")
    assert (
        result
        == "Sorry! I did not find anything for <strong><em>bohemianraphsody!@@</em></strong> 😟"
    )
