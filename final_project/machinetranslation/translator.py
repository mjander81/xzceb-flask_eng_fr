import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
wts_version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=wts_version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''
        Takes a string parameter english_text which represents
        a string of text in the English language and returns
        a string representing the same text in the French 
        language
    '''
    response = language_translator.translate(text=english_text, model='en-fr')
    status_code = response.get_status_code()
    if (status_code == 200):
        french_text = response.get_result()['translations'][0]['translation']
        return french_text
    else:
        return (f"Error: status code {status_code}")

def frenchToEnglish(french_text):
    '''
        Takes a string parameter french_text which represents
        a string of text in the French language and returns
        a string representing the same text in the English 
        language
    '''
    response = language_translator.translate(text=french_text, model='fr-en')
    status_code = response.get_status_code()
    if (status_code == 200):
        english_text = response.get_result()['translations'][0]['translation']
        return english_text
    else:
        return(f"Error: status code {status_code}")