from wation import Wation
from ..miscellaneous import server

def arg_profile(args):
    wation = Wation.instance()
    profile = wation.profile()
    if profile['status'] == True:
        server.sync_config()
        print(f'[+] Profile information :\n')

        print(f"\t[+] Username : {profile['data']['username']}")
    else:
        print(f'[-] Problem occurred with removing session, please try login again.')
