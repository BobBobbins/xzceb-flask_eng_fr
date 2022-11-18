"""This module translates text between french and english"""
import os
import pathlib

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

path_to_env = pathlib.Path(__file__).resolve().parent / ".env"
load_dotenv(path_to_env)

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(f"{apikey}")
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(f"{url}")


def english_to_french(english_text):
    """
    This function translates english to french.
    """

    if not english_text:
        return ""
    response = language_translator.translate(
        text=[english_text], source="en", target="fr"
    ).get_result()
    french_text = response["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """
    This function translates french to english.
    """

    if not french_text:
        return ""
    response = language_translator.translate(
        text=[french_text], source="fr", target="en"
    ).get_result()
    english_text = response["translations"][0]["translation"]
    return english_text
