from item_store import ItemStore
from predict import predict_text
from translate import translate_text


def is_russian(text):
    try:
        text.decode('ascii')
        return False
    except (UnicodeDecodeError, UnicodeEncodeError):
        return True


def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)


def translate(query):

    prediction = predict_text(query).encode('utf-8')
    print 'prediction = ' + prediction

    result = translate_text(prediction)
    print 'translate_prediction = ' + str(result)

    store = ItemStore()
    for text in result['text']:
        sub = '' if query == prediction else prediction
        sub = sub.decode('utf-8')
        text = text.decode('utf-8')
        print 'sub = ' + sub
        print 'text = ' + text

        store.add_item(
                    title = text,
                    subtitle = sub,
                    icon = get_text_icon(text))
    return store


# for debug only
if __name__ == '__main__':

    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hello world'

    query.decode('utf-8')

    print translate(query)
