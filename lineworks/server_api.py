#  cording: utf-8
"""Preparing for API authentication and calling the server API

Issue an access token using the server ID issued in the Developer Console and call the server API.
For more information, please refer to the official documentation.

Preparing for API authentication
URL:https://developers.worksmobile.com/jp/document/1002002?lang-ja

Calling the API
URL:https://developers.worksmobile.com/jp/document/3002003?lang-ja
"""
import datetime
from datetime import datetime, timedelta
import json
import logging

import jwt
import requests


logger = logging.getLogger(__name__)


class ServerApi(object):
    """This is the base class of API that use server APIs( e.g. Talk Bot API).

    The LINE WORKS Bot Platform API is divided into two types: the Service API and the Server API.
    Server API is an API that does not require a user to log in.
    You can access all user data in the domain.

    Attributes:
        api_id: API ID of your domain issued by LINE WORKS Developer Console.
        server_api_consumer_key: The consumer key of the server API issued by the LINE WORKS Developer Console.
        server_id: Id of the server you added in the Server List (IDENTITY registration type).
        private_key: When you issue a server ID in the Server List (identity registration type), the authentication key
                    is issued for each server.
        domain_id: Your domain id.
    """
    def __init__(self, api_id, server_api_consumer_key, server_id, private_key, domain_id):
        """Constructor"""
        self.api_id = api_id
        self.server_api_consumer_key = server_api_consumer_key
        self.server_id = server_id
        self.private_key = private_key
        self.domain_id = domain_id

    def get_access_token(self):
        """Gets an access token to call the server API. (Identity Registration Type)

        An authentication format that issues tokens using the server ID issued in the Developer Console.
        Issue Token by calling "two-legged OAuth 2.0 API" using JWT (JSON Web Token RFC-7519).
        For more information, see the official documentation.
        URL:https://developers.worksmobile.com/jp/document/1002002?lang-ja

        Returns:
            str: The access token.

        Raises:
            If the access token cannot be obtained, there is no parameter "access_token" in the HTTP response,
            so it will be KeyError.
            In that case, an HTTP response is returned so that the error message can be checked.
        """
        # JWT generation/electronic signature
        iat = int(datetime.now().timestamp())
        exp = int((datetime.now() + timedelta(minutes=30)).timestamp())
        json_claim_set = {
            "iss": self.server_id,
            "iat": iat,
            "exp": exp
        }
        json_header = {"alg": "RS256", "typ": "JWT"}
        lw_jwt = jwt.encode(json_claim_set, self.private_key, algorithm="RS256", headers=json_header)

        # Token Request to LINE WORKS Authentication Server
        url = f"https://auth.worksmobile.com/b/{self.api_id}/server/token"
        header = {"Content-Type": "application/json; charset=UTF-8"}
        params = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": lw_jwt
        }
        logger.info({
            "action": "access token request",
            "status": "run",
            "message": "request start."
        })
        response = requests.post(url, headers=header, params=params)
        try:
            access_token = json.loads(response.text)["access_token"]
            logger.info({
                "action": "access token request",
                "status": "success",
                "message": "access_token=" + access_token
            })
            return access_token
        except TypeError:
            logger.info({
                "action": "access token request",
                "status": "fail",
                "message": response.text
            })
            return response

    def call_server_api(self, url, params, method="POST"):
        """Method for using the issued server token.

        Args:
            url(str): Request URL for each API.
            params(dict): The params of each API.
            method(str): Request method. (the default is the POST method.)

        Returns:
            Http Response.
        """
        access_token = self.get_access_token()
        logging.debug(f"access_token={access_token}")
        logging.debug(f"params={params}")
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "consumerKey": self.server_api_consumer_key,
            "Authorization": "Bearer " + access_token
        }
        logger.debug(f"header={header}")
        logger.info({
            "action": "call server api",
            "status": "run",
            "message": "start a call."
        })
        try:
            # Be careful because it will be an error if you set the keyword argument to "params" instead of "data".
            response = requests.request(method, url, headers=header, data=json.dumps(params))
            message = f"status_code:{response.status_code}  text:{response.text}"
            logger.info({
                "action": "call server api",
                "status": "success",
                "message": message
            })
        except:
            logger.info({
                "action": "call server api",
                "status": "fail",
                "message": response.text
            })
        finally:
            return response
