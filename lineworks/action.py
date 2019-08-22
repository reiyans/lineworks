# coding: utf-8


class Action(object):
    ''' A class that generates actions to be used in button templates, etc.

    See the official documentation for more information.
    URL: https://developers.worksmobile.com/document/1005050
    '''

    def postback_action(self, label, data, display_text):
        postback_action = {
            "type": "postback",
            "label": str(label),
            "data": str(data),
            "displayText": str(display_text),
        }
        return postback_action

    def message_action(self, label, text, postback=None):
        message_action = {
            "type": "message",
            "label": str(label),
            "text": str(text),
            "postback": str(postback),
        }
        return message_action

    def uri_action(self, label, uri):
        uri_action = {
            "type": "uri",
            "label": str(label),
            "uri": str(uri),
        }
        return uri_action

    def camera_action(self, label):
        camera_action = {
            "type": "camera",
            "label": str(label),
        }
        return camera_action

    def camera_roll_action(self, label):
        camera_roll_action = {
            "type": "cameraRoll",
            "label": str(label),
        }
        return camera_roll_action

    def location_action(self, label):
        location_action = {
            "type": "location",
            "label": str(label),
        }
        return location_action

    def generate_actions(self, *args):
        actions = []
        for arg in args:
            actions.append(arg)
        return actions