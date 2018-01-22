from item_store import ItemStore
from lang import is_russian
from predict import predict_text
from translate import translate_text
from dictionary import lookup_text
from multiprocessing import Pool


def get_text_icon(text):
    icon_postfix = 'ru' if is_russian(text) else 'en'
    return 'icons/icon_{}.png'.format(icon_postfix)


def get_translation_result(text):
    pool = Pool(processes=2)

    arg = [ text ]
    translation_request = pool.map_async(translate_text, arg)
    lookup_request = pool.map_async(lookup_text, arg)

    translation_result = translation_request.get()[0]
    lookup_result = lookup_request.get()[0]

    pool.close()
    pool.join()

    return lookup_result if lookup_result else translation_result


def translate(query):
    prediction = predict_text(query)
    result = get_translation_result(prediction)

    subtitle = '' if query == prediction else prediction
    subtitle = subtitle.decode('utf-8')

    store = ItemStore()
    for text in result:
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
