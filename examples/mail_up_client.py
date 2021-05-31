#import pycurl
import json
import base64
import time
import requests
from urllib.parse import quote_plus
from io import BytesIO
#from flask import jsonify


class MailUpException(Exception):
    def __init__(self, code=None, error=None):
        super().__init__(error)
        self.code = code
        self.error = error


class MailUpClient:
    def __init__(self, config):
        self.list_id = config.get('ID_LIST', 1)
        self.logon_endpoint = config.get('LOGON_URI', None)
        self.authorization_endpoint = config.get('AUTH_URI', None)
        self.token_endpoint = config.get('TOKEN_URI', None)
        self.console_endpoint = config.get('CONSOLE_URI', None)
        self.mail_statistics_endpoint = config.get('MAIL_STATS_URI', None)

        self.client_id = config.get('CLIENT_ID', None)
        self.client_secret = config.get('CLIENT_SECRET', None)
        self.callback_uri = config.get('CALLBACK_URI', None)

        self.error_url = None

        self.access_token = None
        self.refresh_token = None
        self.token_time = 0

    def clear_tokens(self):
        self.access_token = None
        self.refresh_token = None
        self.token_time = 0

    def save_token(self, result):
        self.access_token = result.get('access_token', None)
        self.refresh_token = result.get('refresh_token', None)
        self.token_time = time.time() + result.get('expires_in', 0)

    def load_token(self, cookies):
        self.access_token = cookies.get('access_token', None)
        self.refresh_token = cookies.get('refresh_token', None)
        self.token_time = cookies.get('token_time', 0)

    def get_token_time(self):
        return max(0, int(float(self.token_time) - time.time()))

    def get_logon_uri(self):
        return f'{self.logon_endpoint}?client_id={self.client_id}' \
               f'&client_secret={self.client_secret}&response_type=code' \
               f'&redirect_uri={self.callback_uri}'

    def retrieve_access_token(self, login, password):
        url = self.token_endpoint

        body = f'client_id={self.client_id}&client_secret={self.client_secret}' \
               f'&refresh_token={self.refresh_token}&grant_type=refresh_token'

        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Content-length': {len(body)}
                  }

        response = requests.get(url, headers=headers, params=body)
        print ("status code: ", response.status_code)

        if response.status_code != 200 and response.status_code != 302:
                raise MailUpException(code=response.status_code, error="Authorization error")

        #result = json.loads(body)

        #self.save_token(result)