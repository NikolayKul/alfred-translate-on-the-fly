from item_store import ItemStore
import urllib
import urllib2
import json


TRANSLATE_API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
TRANSLATE_API_KEY = 'trnsl.1.1.20180108T204339Z.bd63133ee1faca13.5e5d65d48b26e37678d2c84ecfe2c195e3cabf9d'

PREDICT_API_URL = 'https://predictor.yandex.net/api/v1/predict.json/complete'
PREDICT_API_KEY = 'pdct.1.1.20180115T142706Z.a5c4f724bf141b22.3d432baa9167feaac0c9115667d4a95092b6af82'


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


def get_query_lang(query):
    return 'ru' if is_russian(query) else 'en'


def api_predict(query):
    data = urllib.urlencode({
        'key': PREDICT_API_KEY,
        'lang': get_query_lang(query),
        'q': query
    })
    request = urllib2.urlopen(PREDICT_API_URL, data)
    return json.loads(request.read())


def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)


def translate(query):
    result = api_translate(query)
    store = ItemStore()
    for text in result['text']:
        store.add_item(
                    title = text,
                    subtitle = '',
                    icon = get_text_icon(text))
    print store


# for debug only
if __name__ == '__main__':

    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hello world'

    predict = api_predict(query)
    print json.dumps(predict, ensure_ascii=False)


    #result = api_translate(query)
    #print 'icons = ' + str([get_text_icon(x) for x in result['text']])
    #print 'result = ' + json.dumps(result, ensure_ascii=False)
