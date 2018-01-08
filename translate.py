from item_store import ItemStore

def translate(query):
  """
  Test translate
  """
  return "test"

if __name__ == '__main__':
    f = ItemStore()
    for i in range(0, 10):
        f.add_item('title_{}'.format(i), 'subtitle_{}'.format(i))
    print f
