from item_store import ItemStore
import urllib
import urllib2
import json



TRANSLATE_API_KEY = 'trnsl.1.1.20180108T204339Z.bd63133ee1faca13.5e5d65d48b26e37678d2c84ecfe2c195e3cabf9d'
TRANSLATE_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'



def create_url(query):
    data = urllib.urlencode({
        'key' : TRANSLATE_API_KEY,
        'lang' : 'en-ru'
    })
    return '{}?{}'.format(TRANSLATE_URL, data)



def call_api(query):
    url = create_url(query)
    data = urllib.urlencode({
        'text' : query
    })
    request = urllib2.urlopen(url, data)
    result = json.dumps(request.read(), ensure_ascii=False)
    return result



def translate(query):
    store = ItemStore()

    # just print a `query` for now
    for i in range(0, 10):
        store.add_item(
                '{}_{}'.format(query, i),
                '{}_sub_{}'.format(query, i))

    print store



# for debug only
if __name__ == '__main__':
    print call_api("Hello world!")
