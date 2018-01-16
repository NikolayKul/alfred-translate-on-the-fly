from item_store import ItemStore
from lang import is_russian
from predict import predict_text
from translate import translate_text


def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)


def translate(query):
    prediction = predict_text(query)
    result = translate_text(prediction)
    store = ItemStore()
    for text in result['text']:
        subtitle = '' if query == prediction else prediction
        subtitle = subtitle.decode('utf-8')
        store.add_item(
                    title = text,
                    subtitle = subtitle,
                    icon = get_text_icon(text))
    return store


# for debug only
if __name__ == '__main__':

    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hello world'
    print translate(query)
