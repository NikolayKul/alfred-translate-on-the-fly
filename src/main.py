from item_store import ItemStore
from lang import is_russian
from predict import predict_text
from translate import translate_text


def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)


def print_debug_info(name, value):
    print '{} = {}, isUnicode = {}'.format(name, value, isinstance(value, unicode))


def translate(query):
    print_debug_info('query', query)

    prediction = predict_text(query)
    print_debug_info('prediction', prediction)

    result = translate_text(prediction)
    print 'translate = ' + str(result)

    store = ItemStore()
    for text in result['text']:
        sub = '' if query == prediction else prediction
        sub = sub.decode('utf-8')

        print 'sub = ' + sub
        print 'sub is Unicode = ' + str(isinstance(sub, unicode))
        print 'text = ' + text
        print 'text is Unicode = ' + str(isinstance(text, unicode))

        store.add_item(
                    title = text,
                    subtitle = sub,
                    icon = get_text_icon(text))
    return store


# for debug only
if __name__ == '__main__':

    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hello world'
    print translate(query)
