from lang import get_translation_lang
import urllib
import urllib2
import json


TRANSLATE_API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
TRANSLATE_API_KEY = 'trnsl.1.1.20180108T204339Z.bd63133ee1faca13.5e5d65d48b26e37678d2c84ecfe2c195e3cabf9d'


def _api_translate_text(text):
    data = urllib.urlencode({
        'key' : TRANSLATE_API_KEY,
        'lang' : get_translation_lang(text),
        'text' : text
    })
    request = urllib2.urlopen(TRANSLATE_API_URL, data)
    return json.loads(request.read())


def translate_text(text):
    translation = _api_translate_text(text)
    return translation['text']
