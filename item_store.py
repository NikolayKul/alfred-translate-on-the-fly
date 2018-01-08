import xml.etree.ElementTree as et

class _Item(object):
    """Alfred's row item"""

    def __init__(self, title, subtitle, icon='icon.png'):
        self.title = title
        self.subtitle = subtitle
        self.icon = icon

    def __str__(self):
        return et.tostring(self.to_xml())

    def to_xml(self):
        """Returns an `XML` representation of a single `Item` based on https://www.alfredforum.com/topic/5-generating-feedback-in-workflows"""

        et_item = et.Element('item', uid = '', arg = '', valid = 'yes', autocomplete = '')
        et_title = et.SubElement(et_item, 'title')
        et_title.text = self.title
        et_subtitle = et.SubElement(et_item, 'subtitle')
        et_subtitle.text = self.subtitle
        et_icon = et.SubElement(et_item, 'icon')
        et_icon.text = self.icon
        return et_item


class ItemStore(object):

    def __init__(self):
        self.items = []

    def __str__(self):
        return et.tostring(self.to_xml())

    def add_item(self, title, subtitle):
        it = _Item(title, subtitle)
        self.items.append(it)

    def to_xml(self):
        """Returns an `XML` representation of all `Item`s"""

        root = et.Element('items')
        for item in self.items:
            root.append(item.to_xml())
        return root
