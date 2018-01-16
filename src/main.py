from item_store import ItemStore
from predict import predict_text
import urllib
import urllib2
import json


TRANSLATE_API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
TRANSLATE_API_KEY = 'trnsl.1.1.20180108T204339Z.bd63133ee1faca13.5e5d65d48b26e37678d2c84ecfe2c195e3cabf9d'


def is_russian(query):
    try:
        query.decode('ascii')
        return False
    except (UnicodeDecodeError, UnicodeEncodeError):
        return True


def get_translate_lang(query):
    return 'ru-en' if is_russian(query) else 'en-ru'


def api_translate(query):
    data = urllib.urlencode({
        'key' : TRANSLATE_API_KEY,
        'lang' : get_translate_lang(query),
        'text' : query
    })
    request = urllib2.urlopen(TRANSLATE_API_URL, data)
    return json.loads(request.read())


def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)


def translate(query):
    prediction = predict_text(query).encode('utf-8')
    print 'prediction = ' + prediction
    result = api_translate(prediction)
    print 'result_with_pred = ' + str(result)
    store = ItemStore()
    for text in result['text']:
        sub = '' if query == prediction else prediction
        print 'sub = ' + sub.decode('utf-8')
        print 'text = ' + text.decode('utf-8')
        store.add_item(
                    title = text.decode('utf-8'),
                    subtitle = sub.decode('utf-8'),
                    icon = get_text_icon(text))
    return store


# for debug only
if __name__ == '__main__':

    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hello world'

    query.decode('utf-8')

    print translate(query)
