from item_store import ItemStore

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
    store = ItemStore()
    for i in range(0, 10):
        store.add_item(
                'title_{}'.format(i),
                'subtitle_{}'.format(i))
    print store
