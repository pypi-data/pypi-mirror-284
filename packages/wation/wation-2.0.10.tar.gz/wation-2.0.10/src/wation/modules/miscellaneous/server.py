from wation.modules.miscellaneous import auth
from wation.modules.miscellaneous import config
from wation import Wation
import sys
import time

def sync_config():
    wation = Wation.instance()
    response = wation.request('/config', 'get')
    if response['status'] != True:
        auth.logout()
        sys.exit("[-] Problem occurred with getting config, please try login again.")

    config.set_items({
        "features": response['data']['features'],
        "package_last_version": response['data']['package_last_version'],
        "last_sync": time.time(),
    })

    return True