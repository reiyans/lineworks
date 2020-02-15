#  cording: utf-8
"""Talk Bot API

The Talk Bot API allows you to send and receive messages from your talk bot account to your members.
For example, you can communicate interactively between a message sending and receiving server and members that
you have prepared, or you can automatically reply to a talk sent by a member.
For more information, please refer to the official documentation.
URL:https://developers.worksmobile.com/jp/document/3005001?lang-ja
"""
import logging
from logging.config import fileConfig

from .server_api import ServerApi


fileConfig(r".\logging.ini")
logger = logging.getLogger()


class TalkBotApi(ServerApi):
    """Talk Bot API class."""
    def __init__(self, api_id, server_api_consumer_key, server_id, private_key, domain_id, bot_no):
        """Constructor"""
        super().__init__(api_id, server_api_consumer_key, server_id, private_key, domain_id)
        self.bot_no = bot_no

    def register_bot(self, name, photo_url, description, managers, sub_managers=None, use_group_join=None,
                     use_domain_scope=None, domain_ids=None, use_callback=None, callback_url=None,
                     callback_events=None):
        """Talk bot tenant registration.

        Register the Talk Bot with the tenant.
        In order to actually use Talk Bot, you need to register for each domain in addition to tenant registration.

        Args:
            name(str): Talk Bot name.
            photo_url(str): Profile photo of Talk Bot.
            description(str): Description of Talk Bot.
            managers(list): Talk Bot rep's LINE WORKS account list (one is required. Up to 3 people).
            sub_managers(list): Talk Bot Deputy Line WORKS Account List for up to 3 people.
            use_group_join(Bool): How to invite people to talk room.
                                    ● true: Invited to multiple talk rooms
                                    ● false: 1:1 talk only (default)
            use_domain_scope(Bool): Talk Bot Coverage
                                    ● true: specified domainonly
                                    ● false: All domains (default)
            domain_ids(str): If useDomainScope is true, one or more specified domain lists are required.
            use_callback(Bool): Using callbacks
                                    ● true: On
                                    ● false: Off (default)
            callback_url(str): The URL of the message receiving server. Required if useCallback is true. HTTPS only.
            callback_events(Action Obj): The message type that a member can send:text, location, sticker or image.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot"
        payload = {
            "name": name,
            "photoUrl": photo_url,
            "description": description,
            "managers": managers,
            "submanagers": sub_managers,
            "useGroupJoin": use_group_join,
            "useDomainScope": use_domain_scope,
            "domainIds": domain_ids,
            "useCallback": use_callback,
            "callbackUrl": callback_url,
            "callbackEvents": callback_events,
        }
        response = self.call_server_api(url, payload)
        return response

    def bot_fix(self, name, photo_url, description, managers, sub_managers=None, use_group_join=None,
                use_domain_scope=None, domain_ids=None, use_callback=None, callback_url=None, callback_events=None):
        """Talk bot tenant registration.

        Register the Talk Bot with the tenant.
        In order to actually use Talk Bot, you need to register for each domain in addition to tenant registration.

        Args:
            name(str): Talk Bot name.
            photo_url(str): Profile photo of Talk Bot.
            description(str): Description of Talk Bot.
            managers(list): Talk Bot rep's LINE WORKS account list (one is required. Up to 3 people).
            sub_managers(list): Talk Bot Deputy Line WORKS Account List for up to 3 people.
            use_group_join(Bool): How to invite people to talk room.
                                    ● true: Invited to multiple talk rooms
                                    ● false: 1:1 talk only (default)
            use_domain_scope(Bool): Talk Bot Coverage
                                    ● true: specified domainonly
                                    ● false: All domains (default)
            domain_ids(str): If useDomainScope is true, one or more specified domain lists are required.
            use_callback(Bool): Using callbacks
                                    ● true: On
                                    ● false: Off (default)
            callback_url(str): The URL of the message receiving server. Required if useCallback is true. HTTPS only.
            callback_events(Action Obj): The message type that a member can send:text, location, sticker or image.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}"
        payload = {
            "name": name,
            "photoUrl": photo_url,
            "description": description,
            "managers": managers,
            "submanagers": sub_managers,
            "useGroupJoin": use_group_join,
            "useDomainScope": use_domain_scope,
            "domainIds": domain_ids,
            "useCallback": use_callback,
            "callbackUrl": callback_url,
            "callbackEvents": callback_events,
        }
        response = self.call_server_api(url, payload, "PUT")
        return response

    def remove_bot(self):
        """Remove the bot.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}"
        payload = {"botNo": self.bot_no}
        response = self.call_server_api(url, payload, "DELETE")
        return response

    def query_bot_list(self):
        """Queries the list of talk bots.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot"
        response = self.call_server_api(url, payload=None, method="GET")
        return response

    def query_bot_info(self):
        """Queries the talk bot info.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}"
        payload = {'botNo': self.bot_no}
        response = self.call_server_api(url, payload, "GET")
        return response

    def bot_domain_registration(self, use_public=False, use_permission=False, account_ids=None):
        """Register the bot with the domain.

        Args:
            use_public(Bool): Publish to Bot List
                                ● true: Publish
                                ● false: Private (default)
            use_permission(Bool): Bot usage rights
                                ● true: Member specification
                                ● false: All (default)
            account_ids(list): If usePermission is true, the member list.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/domain/{self.domain_id}"
        payload = {
            "usePublic": use_public,
            "usePermission": use_permission,
            "accountIds": account_ids,
        }
        response = self.call_server_api(url, payload)
        return response

    def bot_domain_fix(self, use_public=False, use_permission=False, account_ids=None):
        """Fix bot domain publishing settings.

        Args:
            use_public(Bool): Publish to Bot List
                                ● true: Publish
                                ● false: Private (default)
            use_permission(Bool): Bot usage rights
                                ● true: Member specification
                                ● false: All (default)
            account_ids(list): If usePermission is true, the member list.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/domain/{self.domain_id}"
        payload = {
            "usePublic": use_public,
            "usePermission": use_permission,
            "accountIds": account_ids,
        }
        response = self.call_server_api(url, payload, "PUT")
        return response

    def bot_domain_delete(self):
        """Removes the Talk Bot from a specific domain.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/domain/{self.domain_id}"
        payload = {
            "botNo": self.bot_no,
            "domainId": self.domain_id
        }
        response = self.call_server_api(url, payload, "DELETE")
        return response

    def create_room(self, account_ids, title):
        """Create a new talk room with a private Bot.

        By line works specification, you must publish the Bot to all users before you can invite it to an existing
        talk room.
        Use this method to create a talk room that contains a private Bot.

        Args:
            account_ids(list): Your team members account.
            title(str): Your room title

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/room"
        payload = {
            "accountIds": account_ids,
            "title": title
        }
        response = self.call_server_api(url, payload)
        return response

    def query_room_member_list(self, room_id):
        """Queries the list of members of the talk room that the Bot is participating in.

        Args:
            room_id(str): The room id.
        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/room/{room_id}/accounts"
        payload = {
            "botNo": self.bot_no,
            "roomId": str(room_id)
        }
        response = self.call_server_api(url, payload, "GET")
        return response

    def bot_leaving_room(self, room_id):
        """Leave the Bot from the specified talk room.

        Args:
            room_id(str): The room id.

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/room/{room_id}/leave"
        payload = {
            "botNo": self.bot_no,
            "roomId": str(room_id)
        }
        response = self.call_server_api(url, payload)
        return response

    def send_message(self, content, account_id=None, room_id=None, quick_reply_items=None):
        """The base method for sending messages.

        You can change the contents of the message by changing the argument (content).

        Args:
            content(dict): The content of the message.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        url = f"https://apis.worksmobile.com/r/{self.api_id}/message/v1/bot/{self.bot_no}/message/push"
        payload = {"botNo": str(self.bot_no)}

        # accountId and roomId specify one or the other.
        if account_id is not None:
            payload.update({"accountId": str(account_id)})
        elif room_id is not None:
            payload.update({"roomId": str(room_id)})
        else:
            print("Please specify either account_id or room_id.")
        payload.update(content)
        if quick_reply_items is not None:
            payload["content"].update({"quickReply": {"items": quick_reply_items}})
        response = self.call_server_api(url, payload)
        return response

    def send_text_message(self, send_text, account_id=None, room_id=None, quick_reply_items=None):
        """Send a text message.

        Args:
            send_text(str): Messages sent to Talk Bot.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        content = {
            "content": {
                "type": "text",
                "text": send_text
            }
        }
        response = self.send_message(content, account_id, room_id, quick_reply_items)
        return response

    def send_image(self, preview_resource_url=None, resource_id=None, account_id=None, room_id=None,
                   quick_reply_items=None):
        """Send a picture.

        Args:
            preview_resource_url(str): Preview and the original image URL (PNG format, HTTPS only).
            resource_id(str): Resource ID.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        if preview_resource_url is not None:
            content = {
                "content": {
                    "type": "image",
                    "previewUrl": str(preview_resource_url),
                    "resourceUrl": str(preview_resource_url),
                }
            }
        elif resource_id is not None:
            content = {
                "content": {
                    "type": "image",
                    "resourceId": str(resource_id),
                }
            }
        else:
            return "Please specify either previewUrl/resourceUrl or resourceId."
        response = self.send_message(content, account_id, room_id, quick_reply_items)
        return response

    def send_link(self, content_text, link_text, link, account_id=None, room_id=None, quick_reply_items=None):
        """Use the Talk Bot to send a link message.

        Args:
            content_text(str): Body text.
            link_text(str): The text of the link.
            link(str): URL to transition when linkText click.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        content = {
            "content": {
                "type": "link",
                "contentText": str(content_text),
                "linkText": str(link_text),
                "link": str(link),
            }
        }
        response = self.send_message(content, account_id, room_id, quick_reply_items)
        return response

    def send_sticker(self, package_id, sticker_id, account_id=None, room_id=None, quick_reply_items=None):
        """Send stamps using talk bot.

        Use the Talk Bot to send a stamp.
        See stamp list for details on the package ID/stamp ID for each stamp.
        Stamp List URL: https://static.worksmobile.net/static/wm/media/message-bot-api/line_works_sticker_list_new.pdf

        Args:
            package_id(str): The package ID of the stamp list.
            sticker_id(str): The sticker ID of the stamp list.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        content = {
            "content": {
                "type": "sticker",
                "packageId": str(package_id),
                "stickerId": str(sticker_id),
            }
        }
        response = self.send_message(content, account_id, room_id, quick_reply_items)
        return response

    def send_button_template(self, content_text, actions, account_id=None, room_id=None, quick_reply_items=None):
        """Submit a button template using talk bot.

        Use the Talk Bot to submit a button template.
        When a member presses a button, the text of the button label and the message specified in postback are sent to
        the Bot receiving server.

        Args:
            content_text(str): The text to display on the button.
            actions(Obj): The button list.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        content = {
            "content": {
                "type": "button_template",
                "contentText": str(content_text),
                "actions": actions,
            }
        }
        response = self.send_message(content, account_id, room_id, quick_reply_items)
        return response

    def send_list_template(self, elements, cover_data=None, actions=None, account_id=None, room_id=None,
                           quick_reply_items=None):
        """Use the Talk Bot to submit a list template.

        Args:
            elements(list): Item list.
            cover_data(obj): Cover data.
            actions(obj): The button at the bottom.
                          The first array represents a row, and the second array represents a column.
            account_id(str): The account ID to which you want to send the message.
            room_id(str): The account ID to which you want to send the message.
            quick_reply_items(obj):  An instance of the Quick Reply Item class (optional).

        Returns:
            Http response.
        """
        content = {
            "content": {
                "type": "list_template",
                "coverData": cover_data,
                "elements": elements,
                "actions": actions,
            }
        }
        response = self.send_message(content, account_id, room_id, quick_reply_items)
        return response
