# coding: utf-8


class QuickReplyItems(object):
    ''' A class that generates items required for a quick reply object.

    See the official documentation for more information.
    URL: https://developers.worksmobile.com/document/100500807
    '''

    def generate_item(self, action, image_url=None):
        item = {
            "imageUrl": image_url,
            "action": action,
        }
        return item

    def generate_items(self, *args):
        items = []
        for item in args:
            items.append(item)
        return items