import sys
import time
import os
from wation import Wation

def share(filename, content, uid=None):
    return wation.request('/share', 'post', {
        "filename": filename,
        "content": content,
        "uid": uid
    })

def main(args):
    global wation

    if not os.path.exists(args.filepath):
        print(f'[-] Target file {args.filepath} not found.')
        sys.exit()

    wation = Wation.instance()

    loop_status = True
    last_modified = None
    uid = None
    while loop_status:
        current_modified = os.path.getmtime(args.filepath)
        if current_modified != last_modified:
            last_modified = current_modified
            try:
                with open(args.filepath, 'rb') as f:
                    file_content = f.read().decode('utf-8')
            except UnicodeDecodeError:
                sys.exit("[-] Target file does not appear to be a valid plaintext file.")
            
            print(f"[~] File {args.filepath} has been changed.")

            print(f"[~] Sync progress starts...")
            filename = os.path.basename(args.filepath)
            response = share(filename, file_content, uid)

            if uid == None:
                uid = response['data']['uid']

            print(f"[+] File {args.filepath} has been updated.")
        if args.live == True:
            time.sleep(1)
        else:
            loop_status = False