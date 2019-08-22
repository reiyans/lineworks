#  cording:utf-8

import json

from .server_api import ServerApi


class TalkBotApi(ServerApi):
    ''' Talkbot API class.

    Currently, the features that can be implemented are as follows:

    ・Create, delete bots and register with domains.
    ・Create a private talk bot and a talk room with multiple users
    ・Some features of sending messages.
    '''

    def __init__(self, api_id, private_key, server_api_consumer_key, server_id, bot_no, domain_id, account_id=None, room_id=None):
        ''' Constructor '''
        super().__init__(api_id, private_key, server_api_consumer_key, server_id)
        self.BOT_NO = bot_no
        self.ACCOUNT_ID = account_id
        self.ROOM_ID = room_id
        self.DOMAIN_ID = domain_id

    def register_bot(self, name, photo_url, description, managers, sub_managers=None, use_group_join=None,
                                use_domain_scope=None, domain_ids=None, use_callback=None, callback_url=None,
                                callback_events=None):
        ''' Talk bot tenant registration.

        Register the Talk Bot with the tenant.
        In order to actually use Talk Bot, you need to register for each domain in addition to tenant registration.

        :param name(str): Talk Bot name.
        :param photo_url(str): Profile photo of Talk Bot.
        :param description(str): Description of Talk Bot.
        :param managers[list]: Talk Bot rep's LINE WORKS account list (one is required. Up to 3 people).
        :param sub_managers(list): Talk Bot Deputy Line WORKS Account List for up to 3 people.
        :param use_group_join(Bool): How to invite people to talk room.
                                ● true: Invited to multiple talk rooms
                                ● false: 1:1 talk only (default)
        :param use_domain_scope(Bool): Talk Bot Coverage
                                ● true: specified domainonly
                                ● false: All domains (default)
        :param domain_ids(str): If useDomainScope is true, one or more specified domain lists are required.
        :param use_callback(Bool): Using callbacks
                                ● true: On
                                ● false: Off (default)
        :param callback_url(str): The URL of the message receiving server. Required if useCallback is true. HTTPS only.
        :param callback_events(Action Obj): The message type that a member can send:text, location, sticker or image.

        :return(dict): BOT NO
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot".format(self.API_ID)
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
        bot_no = json.loads(self.use_server_api(request_url=request_url, payload=payload))
        print(bot_no)
        return bot_no

    def bot_fix(self, name, photo_url, description, managers, sub_managers=None, use_group_join=None,
                                use_domain_scope=None, domain_ids=None, use_callback=None, callback_url=None,
                                callback_events=None):
        ''' Talk bot tenant registration.

        Register the Talk Bot with the tenant.
        In order to actually use Talk Bot, you need to register for each domain in addition to tenant registration.

        :param name(str): Talk Bot name.
        :param photo_url(str): Profile photo of Talk Bot.
        :param description(str): Description of Talk Bot.
        :param managers[list]: Talk Bot rep's LINE WORKS account list (one is required. Up to 3 people).
        :param sub_managers(list): Talk Bot Deputy Line WORKS Account List for up to 3 people.
        :param use_group_join(Bool): How to invite people to talk room.
                                ● true: Invited to multiple talk rooms
                                ● false: 1:1 talk only (default)
        :param use_domain_scope(Bool): Talk Bot Coverage
                                ● true: specified domainonly
                                ● false: All domains (default)
        :param domain_ids(str): If useDomainScope is true, one or more specified domain lists are required.
        :param use_callback(Bool): Using callbacks
                                ● true: On
                                ● false: Off (default)
        :param callback_url(str): The URL of the message receiving server. Required if useCallback is true. HTTPS only.
        :param callback_events(Action Obj): The message type that a member can send:text, location, sticker or image.

        :return(dict): BOT NO
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}".format(self.API_ID, self.BOT_NO)
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
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload, method="PUT"))
        print(response)
        return response

    def remove_bot(self):
        ''' Remove the bot.

        :return: If the request is successful, code 200.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}".format(self.API_ID, self.BOT_NO)
        payload = {"botNo": self.BOT_NO}
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload, method="DELETE"))
        print(response)
        return response

    def query_bot_list(self):
        ''' Queries the list of talk bots.

        :return: If the call succeeds, it returns HTTP 200 code and talk Bot list information.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot".format(self.API_ID)
        response = json.loads(self.use_server_api(request_url=request_url, payload=None, method="GET"))
        print(response)
        return response

    def query_bot_info(self):
        ''' Queries the talk bot info.

        :return: If the call succeeds, it returns HTTP 200 code and talk Bot information.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}".format(self.API_ID, self.BOT_NO)
        payload = {'botNo': self.BOT_NO}
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload, method="GET"))
        print(response)
        return response

    def bot_domain_registration(self, use_public=False, use_permission=False, account_ids=None):
        ''' Register the bot with the domain.

        :param use_public(Bool): Publish to Bot List
                            ● true: Publish
                            ● false: Private (default)
        :param use_permission(Bool): Bot usage rights
                            ● true: Member specification
                            ● false: All (default)
        :param account_ids(list): If usePermission is true, the member list.

        :return: If the request is successful, code 200.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/domain/{}".format(self.API_ID, self.BOT_NO, self.DOMAIN_ID)
        payload = {
            "usePublic": use_public,
            "usePermission": use_permission,
            "accountIds": account_ids,
        }
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload))
        print(response)
        return response

    def bot_domain_fix(self, use_public=False, use_permission=False, account_ids=None):
        ''' Fix bot domain publishing settings.

        :param use_public(Bool): Publish to Bot List
                            ● true: Publish
                            ● false: Private (default)
        :param use_permission(Bool): Bot usage rights
                            ● true: Member specification
                            ● false: All (default)
        :param account_ids(list): If usePermission is true, the member list.

        :return: If the request is successful, code 200.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/domain/{}".format(self.API_ID, self.BOT_NO, self.DOMAIN_ID)
        payload = {
            "usePublic": use_public,
            "usePermission": use_permission,
            "accountIds": account_ids,
        }
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload, method="PUT"))
        print(response)
        return response

    def bot_domain_delete(self):
        ''' Removes the Talk Bot from a specific domain.

        :return: If the request is successful, code 200.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/domain/{}".format(self.API_ID, self.BOT_NO, self.DOMAIN_ID)
        payload = {
            "botNo": self.BOT_NO,
            "domainId": self.DOMAIN_ID
        }
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload, method="DELETE"))
        print(response)
        return response

    def create_room(self, account_ids, title):
        ''' Create a new talk room with a private Bot.

        By line works specification, you must publish the Bot to all users before you can invite it to an existing talk room.
        Use this method to create a talk room that contains a private Bot.

        :param account_ids(list): Your team members account.
        :param title(str): Your room title

        :return(str): Room Id of the created talk room.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/room".format(self.API_ID, self.BOT_NO)
        payload = {
            "accountIds": account_ids,
            "title": title
        }
        room_id = json.loads(self.use_server_api(request_url=request_url, payload=payload))
        print(room_id)
        return room_id

    def room_query(self):
        ''' Queries the list of members of the talk room that the Bot is participating in.

        :return: If the call succeeds, http 200 code and the member list return the total number of pages.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/room/{}/accounts".format(self.API_ID,
                                                                                                    self.BOT_NO,
                                                                                                    self.ROOM_ID)
        payload = {
            "botNo": self.BOT_NO,
            "roomId": self.ROOM_ID
        }
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload, method="GET"))
        print(response)
        return response

    def room_query(self):
        ''' Leave the Bot from the specified talk room.

        :return: Returns HTTP 200 code if the call succeeds.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/room/{}/leave".format(self.API_ID,
                                                                                                    self.BOT_NO,
                                                                                                    self.ROOM_ID)
        payload = {
            "botNo": self.BOT_NO,
            "roomId": self.ROOM_ID
        }
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload))
        print(response)
        return response

    def send_message(self, content_dict, quick_reply_items=None):
        ''' The base method for sending messages.

        You can change the contents of the message by changing the argument (countent_dict).

        :param content_dict(dict): The content of the message.
        :param quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        :return: If the call succeeds, it returns http 200 code.
        '''
        request_url = "https://apis.worksmobile.com/r/{}/message/v1/bot/{}/message/push".format(self.API_ID, self.BOT_NO)
        payload = {
            "botNo": str(self.BOT_NO),
        }

        # AccountId and roomId specify one or the other.
        if self.ACCOUNT_ID is not None:
            payload.update({"accountId": str(self.ACCOUNT_ID)})
        elif self.ROOM_ID is not None:
            payload.update({"roomId": str(self.ROOM_ID)})
        else:
            print("Please specify either ACCOUNT_ID or ROOM_ID.")
        payload.update(content_dict)
        if quick_reply_items is not None:
            payload["content"].update({"quickReply": {"items": quick_reply_items}})
        response = json.loads(self.use_server_api(request_url=request_url, payload=payload))
        print(response)
        return response

    def send_text_message(self, send_text, quick_reply_items=None):
        ''' Send a text message.

        :param send_text(str): Messages sent to talkbot.
        :param quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        :return: If the call succeeds, it returns http 200 code.
        '''
        content_dict = {
            "content": {
                "type": "text",
                "text": send_text
            }
        }
        self.send_message(content_dict=content_dict, quick_reply_items=quick_reply_items)

    def send_image(self, preview_resource_url=None, resource_id=None, quick_reply_items=None):
        ''' Send a picture.

        :param preview_resource_url(str): Preview and the original image URL (PNG format, HTTPS only).
        :param resource_id(str): Resource ID.
        :param quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        :return: If the call succeeds, it returns http 200 code.
        '''
        if preview_resource_url is not None:
            content_dict = {
                "content": {
                    "type": "image",
                    "previewUrl": str(preview_resource_url),
                    "resourceUrl": str(preview_resource_url),
                }
            }
        elif resource_id is not None:
            content_dict = {
                "content": {
                    "type": "image",
                    "resourceId": str(resource_id),
                }
            }
        else:
            print("Please specify either previewUrl/resourceUrl or resourceId.")
        self.send_message(content_dict=content_dict, quick_reply_items=quick_reply_items)

    def send_link(self, content_text, link_text, link, quick_reply_items=None):
        ''' Use the Talk Bot to send a link message.

        :param content_text: Body text.
        :param link_text: The text of the link.
        :param link: URL to transition when linkText click.
        :param quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        :return: If the call succeeds, it returns http 200 code.
        '''
        content_dict = {
            "content": {
                "type": "link",
                "contentText": str(content_text),
                "linkText": str(link_text),
                "link": str(link),
            }
        }
        self.send_message(content_dict=content_dict, quick_reply_items=quick_reply_items)

    def send_sticker(self, package_id, sticker_id, quick_reply_items=None):
        ''' Send stamps using talk bot.

        Use the Talk Bot to send a stamp.
        See stamp list for details on the package ID/stamp ID for each stamp.
        Stamp List URL: https://static.worksmobile.net/static/wm/media/message-bot-api/line_works_sticker_list_new.pdf

        :param package_id(str): The package ID of the stamp list.
        :param sticker_id(str): The sticker ID of the stamp list.
        :param quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        :return: If the call succeeds, it returns http 200 code.
        '''
        content_dict = {
            "content": {
                "type": "sticker",
                "packageId": str(package_id),
                "stickerId": str(sticker_id),
            }
        }
        self.send_message(content_dict=content_dict, quick_reply_items=quick_reply_items)

    def send_button_template(self, content_text, actions, quick_reply_items=None):
        ''' Submit a button template using talk bot.

        Use the Talk Bot to submit a button template.
        When a member presses a button, the text of the button label and the message specified in postback are sent to the Bot receiving server.

        :param content_text(str): The text to display on the button.
        :param actions(Obj): The button list.
        :param quick_reply_items(Obj): An instance of the Quick Reply Item class (optional).

        :return: If the call succeeds, it returns http 200 code.
        '''
        content_dict = {
            "content": {
                "type": "button_template",
                "contentText": str(content_text),
                "actions": actions,
            }
        }
        self.send_message(content_dict=content_dict, quick_reply_items=quick_reply_items)

    def send_list_template(self, elements, cover_data=None, actions=None, quick_reply_items=None):
        ''' Use the Talk Bot to submit a list template.

        :param elements(list): Item list.
        :param cover_data(obj): Cover data.
        :param actions(obj): The button at the bottom. The first array represents a row, and the second array represents a column.
        :param quick_reply_items(obj):  An instance of the Quick Reply Item class (optional).

        :return: Returns HTTP 200 code if the call succeeds.
        '''
        content_dict = {
            "content": {
                "type": "list_template",
                "coverData": cover_data,
                "elements": elements,
                "actions": actions,
            }
        }
        self.send_message(content_dict=content_dict, quick_reply_items=quick_reply_items)