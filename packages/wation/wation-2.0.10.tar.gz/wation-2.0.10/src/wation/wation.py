import requests
import time
from platform import platform
from urllib.parse import urlencode
import sys
from wation.modules.miscellaneous import config

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance

class Wation(Singleton):
    
    module_name = 'WPM'
    module_version = '2.0.10'
    module_http_header = {}
    base_url = 'https://wation.net/api/ext/v1'
    access_token = None
    verify_ssl_cert = True
    proxy = {}

    def __init__(self, client_id, client_secret, persist_token=True, refresh_token_if_persisted=False):
        self.is_authenticated = False
        self.client_id = client_id
        self.client_secret = client_secret
        self.module_http_header['User-Agent'] = f'{Wation.module_name}/{Wation.module_version} ({platform()};)'
        self.persist_token = persist_token
        
        if self.persist_token and refresh_token_if_persisted == False:
            self.access_token = config.get("access_token")

    def __refresh_access_token(self):
        access_token_response = self.request('/token', 'post', {'client_id' : self.client_id, 'client_secret' : self.client_secret}, auth_required=False)
        if access_token_response['status'] == True:
            self.access_token = access_token_response['data']['access_token']
            if self.persist_token:
                config.set("access_token", self.access_token)
            return True
        
        sys.exit('[-] Failed to obtain access token, ' + access_token_response['data']['message']['body'])

    @staticmethod
    def ping():
        # Headers
        headers = {}
        headers.update(Wation.module_http_header) # Add module http header
        return requests.get(f'{Wation.base_url}/ping', verify=Wation.verify_ssl_cert, headers=headers)

    @staticmethod
    def instance():
        client_id = config.get("client_id")  
        client_secret = config.get("client_secret")  

        if client_id == None or client_secret == None:
            print('[-] Client Id/Secret not found. Please log in to your account to obtain a valid token.')
            sys.exit()

        wation = Wation(client_id, client_secret)
        return wation

    def profile(self):
        return self.request('/profile', 'get')

    def request(self, endpoint, method='get', data={}, auth_required=True, retry=False):

        # Data
        data.update({
            'generated_at' : int(time.time())
        })
        data_query_string = urlencode(data)

        # Headers
        headers = {}

        if auth_required == True:
            if self.access_token == None:
                self.__refresh_access_token()

            try:
                headers['Authorization'] = f'Bearer {self.access_token}'
            except:
                return {'status': False, 'code': 601, 'message': 'api key is malformed.'}
        
        headers.update(Wation.module_http_header) # Add module http header

        request_url = f'{Wation.base_url}{endpoint}'

        if method.lower() == 'get':
            response = requests.get(f'{request_url}?{data_query_string}', headers=headers, verify=Wation.verify_ssl_cert, proxies=Wation.proxy)
        elif method.lower() == 'post':
            response = requests.post(request_url, data=data, headers=headers, verify=Wation.verify_ssl_cert, proxies=Wation.proxy)

        if response.status_code == 429:
            return {'status': False, 'code': 429, 'message': 'We\'re experiencing a high volume of requests from your end right now, and we want to ensure a smooth experience for everyone. Please wait a moment and try again shortly. If this issue persists, feel free to reach out to our support team for assistance.'}

        if response.status_code == 481 or response.status_code == 403:
            return {'status': False, 'code': 481, 'message': 'FireEye Protection blocked your request, if you using any VPN, disconnect and try again.'}

        try:
            response_json = response.json()
            if response_json.get('code') == 419 and not retry:
                # Token is expired, request a new one and retry the request
                self.access_token = None
                self.__refresh_access_token()
                return self.request(endpoint, method, data, auth_required, retry=True)
            if response_json.get('code') == 401:
                config.reset_config()
                
            return response_json
        except Exception as e:
            return {'status': False, 'code': 600, 'message': 'connection error.'}
