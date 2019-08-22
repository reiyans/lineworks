#  cording:utf-8

import base64
import datetime
import json

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class ServerApi(object):
    """ This is the base class of API that use server APIs( e.g. talk bot API).

    The LINE WORKS Bot Platform API is divided into two types: the Service API and the Server API.
    Server API is an API that does not require a user to log in.
    You can access all user data in the domain.

    Attributes:
        API_ID: API ID of your domain issued by LINE WORKS Developer Console.
        SERVER_API_CONSUMER_KEY: The consumer key of the server API issued by the LINE WORKS Developer Console.
        SERVER_ID: Id of the server you added in the Server List (IDENTITY registration type).
        PRIVATE_KEY: When you issue a server ID in the Server List (identity registration type), the authentication key is issued for each server.
    """

    def __init__(self, api_id, private_key, server_api_consumer_key, server_id):
        ''' Constructor '''
        self.API_ID = api_id
        self.PRIVATE_KEY = private_key
        self.SERVER_API_CONSUMER_KEY = server_api_consumer_key
        self.SERVER_ID = server_id

    def jwt_generate(self):
        ''' JWT Generation and JWT Electronic Signature - RFC-7515

        The Server Token in the identity registration expression passes the server ID issued by the Developer Console as a parameter.
        Issue token by calling "two-legged OAuth 2.0 API" using JWT (JSON Web Token RFC-7519).
        This method generates the JWT required to issue the Token.

        :return(str): JWT
        '''

        def dict_to_base64encode(dict_str):
            ''' Converts a dictionary string to a Base64 encoded string.

            After converting the dictionary string to JSON format, it encodes it to UTF-8.
            Base64 encodes it and decodes it to UTF-8.

            :param dict_str(dict): A dictionary string.

            :return(str): Base64 encoded string (UTF-8).
            '''
            json_str = json.dumps(dict_str)
            base64encode = base64.urlsafe_b64encode(json_str.encode('utf-8')).decode('utf-8')
            return base64encode

        def rsa_encrypt(plain_text, PRIVATE_KEY):
            ''' Encrypts a plain text and returns an electronic signature.

            Electronic signatures comply with the JWS (JSON Web Signature RFC-7515) convention.
            The byte array of the JWT header and body generated earlier is encrypted with the RSA SHA-256
            algorithm (RS256 specified by header) using the authentication key downloaded by the Developer Console.

            :param plain_text(str): The text that connects header and body with periods.
            :param PRIVATE_KEY(str): The authentication key downloaded from the Developer Console.

            :return(str): Electronic signature.
            '''
            key = RSA.importKey(PRIVATE_KEY)
            byte_array = plain_text.encode('utf-8')
            digest = SHA256.new(byte_array)
            pkcs = PKCS1_v1_5.new(key)
            signature = pkcs.sign(digest)
            return signature

        dict_header = {
            "alg": "RS256",
            "typ": "JWT"
        }
        base64_header = dict_to_base64encode(dict_str=dict_header)
        dict_claim_set = {
            "iss": self.SERVER_ID,

            # JWT generation date and time. Unix time specified (sec)
            "iat": int(datetime.datetime.now().timestamp()),

            # JWT expiration date and time. Unix time specified (sec)
            "exp": int((datetime.datetime.now() + datetime.timedelta(minutes=30)).timestamp())
        }
        base64_claim_set = dict_to_base64encode(dict_str=dict_claim_set)
        plain_text = base64_header + "." + base64_claim_set
        signature = rsa_encrypt(plain_text=plain_text, PRIVATE_KEY=self.PRIVATE_KEY)
        base64_signature = base64.urlsafe_b64encode(signature).decode('utf-8')
        jwt = plain_text + "." + base64_signature
        return jwt

    def server_token_request(self):
        ''' Token Request to LINE WORKS Authentication Server - RFC-7523

        Request URL: https://auth.worksmobile.com/b/{API ID}/server/token

        HTTP Method:
            POST
            content-type : application/x-www-form-urlencoded; charset=UTF-8

        Request: Post the following items:
            parameter | type | required | description
            --------------------------------------------------
            grant_type | String | Y | The URL-encoded String value(urn:ietf:params:oauth:grant-type:jwt-bearer).
            assertion | String | Y | JWT

        :return(str): Access Token.
        '''
        jwt = self.jwt_generate()
        request_url = "https://auth.worksmobile.com/b/{}/server/token".format(self.API_ID)
        header = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        payload = {
            "grant_type": "urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer",
            "assertion": jwt
        }
        try:
            response = requests.post(url=request_url, headers=header, params=payload)
            server_token = json.loads(response.text)["access_token"]
            return server_token
        except:
            error_code = json.loads(response.text)["code"]
            error_message = json.loads(response.text)["message"]
            return error_code + error_message

    def use_server_api(self, request_url, payload, method="POST"):
        ''' Method for using the issued server token.

        :param request_url: Request URL for each API.
        :param payload: The payload of each API.
        :param method: The method at the time of request. The default is POST.

        :return: Http Response text..
        '''
        SERVER_TOKEN = self.server_token_request()
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            "consumerKey": self.SERVER_API_CONSUMER_KEY,
            "Authorization": "Bearer " + SERVER_TOKEN,
        }
        if method == "GET":
            response = requests.get(url=request_url, headers=header, data=json.dumps(payload))
            return response.text
        elif method == "POST":
            response = requests.post(url=request_url, headers=header, data=json.dumps(payload))
            return response.text
        elif method == "PUT":
            response = requests.put(url=request_url, headers=header, data=json.dumps(payload))
            return response.text
        elif method == "DELETE":
            response = requests.delete(url=request_url, headers=header, data=json.dumps(payload))
            return response.text
        else:
            pass