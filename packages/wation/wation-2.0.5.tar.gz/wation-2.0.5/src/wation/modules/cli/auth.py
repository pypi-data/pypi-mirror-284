import os
import sys
from wation import Wation
from ..miscellaneous import auth

def arg_logout(args):
    try_logout = auth.logout()
    if try_logout == True:
        print('[+] You have successfully signed out.')
    else:
        print(f'[-] Problem occurred in removing session, please try login again.')

def arg_login(args):
    client_id = input("Enter your client ID: ")
    client_secret = input("Enter your client secret: ")
    wation = auth.login(client_id, client_secret, True)

    if isinstance(wation, Wation):
        print('[+] You have successfully signed in to Wation.')
    else:
        print(f'[-] {wation}')
