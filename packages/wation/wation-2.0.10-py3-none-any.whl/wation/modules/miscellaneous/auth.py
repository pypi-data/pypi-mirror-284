from wation import Wation
from . import config
import sys
from . import server

def login(client_id, client_secret, force_login=False):    

    if client_id == None and client_secret == None:
        print('[-] Client Id/Secret not found. Please log in to your account to obtain a valid token.')
        sys.exit()

    wation = Wation(client_id, client_secret, refresh_token_if_persisted=True)
    profile = wation.profile()
    
    if profile['status'] == True:
        config.set_items({
            "client_id": client_id,
            "client_secret": client_secret,
        })

        server.sync_config()

        return wation

def logout():
    try:
        config.reset_config()
        return True
    except:
        return False
