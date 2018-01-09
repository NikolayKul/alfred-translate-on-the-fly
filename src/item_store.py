import xml.etree.ElementTree as et

class Item(object):
    """
    Alfred's row item

    Based on https://www.alfredforum.com/topic/5-generating-feedback-in-workflows
    """

    def __init__(self, title, subtitle):
        self.root = et.Element('item', uid = '', arg = '', valid = 'yes', autocomplete = '')
        et_title = et.SubElement(self.root, 'title')
        et_title.text = title
        et_subtitle = et.SubElement(self.root, 'subtitle')
        et_subtitle.text = subtitle
        et_icon = et.SubElement(self.root, 'icon')
        et_icon.text = 'icon.png'

    def __str__(self):
        return et.tostring(self.root)


class ItemStore(object):

    def __init__(self):
        self.root = et.Element('items')

    def __str__(self):
        return et.tostring(self.root)

    def add_item(self, title, subtitle):
        it = Item(title, subtitle)
        self.root.append(it.root)
