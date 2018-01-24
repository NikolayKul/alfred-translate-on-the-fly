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
    query = query.strip()
    prediction = predict_text(query)
    translations = get_translation_result(prediction)

    subtitle = '' if query == prediction else prediction
    subtitle = subtitle.decode('utf-8')

    # (title, subtitle, icon)
    item_tuples = [ (x, subtitle, get_text_icon(x)) for x in translations ]

    # move 1st item to the end because of Alfred
    if item_tuples:
        item_tuples.append(item_tuples[0])
        del item_tuples[0]

    store = ItemStore()
    for item in item_tuples:
        store.add_item(*item)

    return store


# for debug only
if __name__ == '__main__':
    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hello world'
    print translate(query)
