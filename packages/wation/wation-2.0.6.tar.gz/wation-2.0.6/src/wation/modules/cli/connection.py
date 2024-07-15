import requests
import sys
from wation import Wation

def arg_connection(args):
    try:
        connection_info = requests.get('http://ifconfig.io/all.json').json()
    except:
        print('[-] Connection error, please check your internet connection.')
        sys.exit()
    
    print(f'[~] Connection info :\n')
    print(f'\t[+] IP: {connection_info["ip"]}')
    
    if connection_info['host']:
        print(f'\t[+] Host: {connection_info["host"][:-1]}')
    
    print(f'\t[+] Country: {connection_info["country_code"]}')

    test_connection = Wation.ping().status_code
    if test_connection == 481 or test_connection == 403:
        access_status = f'Blocked'
    else:
        access_status = f'Allowed'

    print(f'\t[+] Access: {access_status}')
