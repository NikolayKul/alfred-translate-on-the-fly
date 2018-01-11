from item_store import ItemStore
import urllib
import urllib2
import json



API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20180108T204339Z.bd63133ee1faca13.5e5d65d48b26e37678d2c84ecfe2c195e3cabf9d'



def is_russian(query):
    try:
        query.decode('ascii')
        return False
    except (UnicodeDecodeError, UnicodeEncodeError):
        return True



def get_translate_lang(query):
    return 'ru-en' if is_russian(query) else 'en-ru'



def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)



def api_translate(query):
    data = urllib.urlencode({
        'key' : API_KEY,
        'lang' : get_translate_lang(query),
        'text' : query
    })
    request = urllib2.urlopen(API_URL, data)
    return json.loads(request.read())



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

    result = api_translate(query)
    print 'icons = ' + str([get_text_icon(x) for x in result['text']])
    print 'result = ' + json.dumps(result, ensure_ascii=False)
