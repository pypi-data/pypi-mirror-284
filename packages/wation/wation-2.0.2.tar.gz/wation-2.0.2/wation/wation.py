import requests
import time
from platform import platform
from urllib.parse import urlencode
import os
import appdirs
import sys

class Wation:
    module_name = 'WPM'
    module_version = '2.0.2'
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

        app_path = appdirs.user_data_dir('Wation','Wation')
        if not os.path.exists(app_path):
            os.makedirs(app_path)
        
        self.token_persist_path = os.path.join(app_path, 'token')
        if self.persist_token and refresh_token_if_persisted == False:
            if os.path.exists(self.token_persist_path):
                with open(self.token_persist_path, 'r') as token_file:
                    self.access_token = token_file.read()

    def __refresh_access_token(self):
        access_token_response = self.__request('/token', 'post', {'client_id' : self.client_id, 'client_secret' : self.client_secret}, auth_required=False)
        if access_token_response['status'] == True:
            self.access_token = access_token_response['data']['access_token']
            if self.persist_token:
                with open(self.token_persist_path, 'w+') as token_file:
                    token_file.write(self.access_token)
            return True
        
        sys.exit('[-] Failed to obtain access token, ' + access_token_response['data']['message']['body'])

    @staticmethod
    def ping():
        return requests.get(f'{Wation.base_url}/ping', verify=Wation.verify_ssl_cert)

    def profile(self):
        return self.__request('/profile', 'get')

    def share(self, filename, content, uid=None):
        return self.__request('/share', 'post', {
            "filename": filename,
            "content": content,
            "uid": uid
        })

    def __request(self, endpoint, method='get', data={}, auth_required=True, retry=False):

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
        
        if response.status_code == 481 or response.status_code == 403:
            return {'status': False, 'code': 481, 'message': 'FireEye Protection blocked your request, if you using any VPN, disconnect and try again.'}
    
        try:
            response_json = response.json()
            if response_json.get('code') == 419 and not retry:
                # Token is expired, request a new one and retry the request
                self.access_token = None
                self.__refresh_access_token()
                return self.__request(endpoint, method, data, auth_required, retry=True)
            return response_json
        except:
            return {'status': False, 'code': 600, 'message': 'connection error.'}
