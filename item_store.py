
class _Item(object):
    """Class that represents an Alfred's row item"""

    def __init__(self, title, subtitle, icon='icon.png'):
        self.title = title
        self.subtitle = subtitle
        self.icon = icon

    def __str__(self):
        return '(Title: {}, Subtitle: {}, Icon: {})' \
            .format(self.title, self.subtitle, self.icon)


class ItemStore(object):

    def __init__(self):
        self.items = []

    def __str__(self):
        s = map(str, self.items)
        return ',\n'.join(s)

    def add_item(self, title, subtitle):
        it = _Item(title, subtitle)
        self.items.append(it)
