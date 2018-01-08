
class Item(object):
    """Class that represents an Alfred's row item"""

    def __init__(self, title, subtitle, icon):
        self.title = title
        self.subtitle = subtitle
        self.icon = icon

    def __str__(self):
        return '(Title: {}, Subtitle: {}, Icon: {})'.format(self.title, self.subtitle, self.icon)


class ItemFactory(object):
    """Factory to store `Items`"""

    default_icon = "stub"

    def __init__(self):
        self.items = []

    def __str__(self):
        s = map(str, self.items)
        return ',\n'.join(s)

    def add_item(self, title, subtitle):
        it = Item(title, subtitle, ItemFactory.default_icon)
        self.items.append(it)

if __name__ == '__main__':
    f = ItemFactory()
    for i in range(0, 10):
        f.add_item('title_{}'.format(i), 'subtitle_{}'.format(i))
    print f
