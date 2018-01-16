import urllib
import urllib2
import json


PREDICT_API_URL = 'https://predictor.yandex.net/api/v1/predict.json/complete'
PREDICT_API_KEY = 'pdct.1.1.20180115T142706Z.a5c4f724bf141b22.3d432baa9167feaac0c9115667d4a95092b6af82'


def is_russian(text):
    try:
        text.decode('ascii')
        return False
    except (UnicodeDecodeError, UnicodeEncodeError):
        return True


def get_lang(text):
    return 'ru' if is_russian(text) else 'en'


def api_predict(query):
    data = urllib.urlencode({
        'key': PREDICT_API_KEY,
        'lang': get_lang(query),
        'q': query
    })
    request = urllib2.urlopen(PREDICT_API_URL, data)
    return json.loads(request.read())


def predict_text(text):
    prediction = api_predict(text)
    decoded_text = text.decode('utf-8')
    pos = len(decoded_text) + prediction['pos']
    return decoded_text[:pos] + prediction['text'][0]
