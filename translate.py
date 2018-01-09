from item_store import ItemStore
import urllib
import urllib2
import json



API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20180108T204339Z.bd63133ee1faca13.5e5d65d48b26e37678d2c84ecfe2c195e3cabf9d'



def api_create_url(query):
    data = urllib.urlencode({
        'key' : API_KEY,
        'lang' : 'en-ru'
    })
    return '{}?{}'.format(API_URL, data)



def api_translate(query):
    url = api_create_url(query)
    data = urllib.urlencode({
        'text' : query
    })
    request = urllib2.urlopen(url, data)
    response = request.read().decode('utf-8')
    return json.loads(response)



def translate(query):
    result = api_translate(query)
    store = ItemStore()
    for text in result['text']:
        store.add_item(text, text)
    print store



# for debug only
if __name__ == '__main__':
    result = api_translate('hello world')
    for text in result['text']:
        print text
