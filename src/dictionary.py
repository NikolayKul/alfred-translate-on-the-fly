from lang import get_translation_lang
import urllib
import urllib2
import json


DICTIONARY_API_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
DICTIONARY_API_KEY = 'dict.1.1.20180117T145511Z.b67b19185537ca0d.545a8ec77182fd03bbc218d50fdbef3c09a1a805'


def _api_lookup_text(text):
    data = urllib.urlencode({
        'key' : DICTIONARY_API_KEY,
        'lang' : get_translation_lang(text),
        'text' : text
    })
    request = urllib2.urlopen(DICTIONARY_API_URL, data)
    return json.loads(request.read())


def lookup_text(text):
    lookup = _api_lookup_text(text)
    if not lookup['def']:
        return []

    first_article = lookup['def'][0]
    first_translations = first_article['tr'][0]

    result = [ first_translations['text'] ]
    if 'syn' in first_translations:
        for syn in first_translations['syn']:
            result.append( syn['text'] )

    return result
