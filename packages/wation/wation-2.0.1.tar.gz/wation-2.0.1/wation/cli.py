#!/usr/bin/env python3

from wation import Wation
import argparse
import sys
import appdirs
import os
import sys
import requests
import webbrowser
import time
import subprocess

def banner():
    print(f'''
  __     __     ______     ______   __     ______     __   __
 /\ \  _ \ \   /\  __ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \\
 \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \\
  \ \__/".~\_\  \ \_\ \_\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\\
   \/_/   \/_/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_/ \/_/
          
    ''')

# define our clear function
def clear_terminal():

    # for windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_wation_instance():  
    client_id = None  
    client_secret = None  
    if os.path.exists(client_persist_path):
        with open(client_persist_path, 'r') as client_file:
            client_secret, client_id = str(client_file.read()).split('@')

    if client_id == None and client_secret == None:
        print('[-] Client Id/Secret not found. Please log in to your account to obtain a valid token.')
        sys.exit()

    wation = Wation(client_id, client_secret)
    return wation

def login(client_id, client_secret, force_login=False):    

    if client_id == None and client_secret == None:
        print('[-] Client Id/Secret not found. Please log in to your account to obtain a valid token.')
        sys.exit()

    wation = Wation(client_id, client_secret, refresh_token_if_persisted=True)
    check_command = wation.profile()

    if check_command['status'] != True:
        return check_command['data']['message']['body']

    with open(client_persist_path, 'w+') as client_file:
        client_file.write(f'{client_secret}@{client_id}')

    return wation

def logout():
    try:
        os.remove(token_persist_path)
        os.remove(client_persist_path)
        return True
    except:
        return False

def arg_logout(args):
    try_logout = logout()
    if try_logout == True:
        print('[+] You have successfully signed out.')
    else:
        print(f'[-] Problem occurred in removing session, please try login again.')

def arg_profile(args):
    wation = get_wation_instance()
    profile = wation.profile()
    if profile['status'] == True:
        print(f'[+] Profile information :\n')
        for profile_key, profile_value in profile['data'].items():
            print(f'\t[+] {profile_key.capitalize()} : {profile_value}')
    else:
        print(f'[-] Problem occurred with removing session, please try login again.')

def arg_login(args):
    client_id = input("Enter your client ID: ")
    client_secret = input("Enter your client secret: ")
    wation = login(client_id, client_secret, True)

    if isinstance(wation, Wation):
        print('[+] You have successfully signed in to Wation.')
    else:
        print(f'[-] {wation}')

def arg_share(args):

    if not os.path.exists(args.filepath):
        print(f'[-] Target file {args.filepath} not found.')
        sys.exit()

    wation = get_wation_instance()

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
            response = wation.share(filename, file_content, uid)

            if uid == None:
                uid = response['data']['uid']

            print(f"[+] File {args.filepath} has been updated.")
        if args.live == True:
            time.sleep(1)
        else:
            loop_status = False

def arg_open(args):
    webbrowser.open_new_tab("https://wation.net")
    print("[+] Wation.net has been opened in the default browser.")

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

def upgrade_package():
    package_name = "wation"  # Replace with your package name
    try:
        # Run the pip install command to upgrade the package
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
        print(f"Package '{package_name}' upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade package '{package_name}'. Error: {e}")

def main():
    global app_path, token_persist_path, client_persist_path
    try:
        clear_terminal()
        banner()
        
        # App Path
        app_path = appdirs.user_data_dir('Wation','Wation')
        if not os.path.exists(app_path):
            os.makedirs(app_path)

        token_persist_path = os.path.join(app_path, 'token')
        client_persist_path = os.path.join(app_path, 'client')

        # parser
        cli_parser = argparse.ArgumentParser(prog='wation', description='Wation CLI Connector.')
        cli_parser.add_argument("--version", "-v", action="version", version=f"[+] Version: v{Wation.module_version}", help="Show version information")
        cli_parser.add_argument("--update", "-u", action="store_true", help="Upgrade the package")
        
        cli_subparsers = cli_parser.add_subparsers(title="subcommands", dest="command", help="Available commands")

        login_command = cli_subparsers.add_parser('login', help="Log in to Wation using your credentials.")
        login_command.set_defaults(func=arg_login)

        logout_command = cli_subparsers.add_parser('logout', help="Log out of your current Wation session.")
        logout_command.set_defaults(func=arg_logout)

        open_command = cli_subparsers.add_parser('open', help="Open Wation.net in the default browser.", description="Open Wation.net in the default browser.")
        open_command.set_defaults(func=arg_open)

        connection_command = cli_subparsers.add_parser('connection', help="Checks your internet connection and the accessibility of Wation.")
        connection_command.set_defaults(func=arg_connection)

        profile_command = cli_subparsers.add_parser('profile', help="Show your profile information.")
        profile_command.set_defaults(func=arg_profile)

        share_command = cli_subparsers.add_parser('share', help="Share the target file with audiences.")
        share_command.add_argument("filepath", type=str, help="Path to the file to actively share")
        share_command.add_argument("--live", action="store_true", help="Monitor the file for changes (default: one-time check)")
        share_command.set_defaults(func=arg_share)

        # if len(sys.argv) <= 1:
        #     sys.argv.append('--help')

        args = cli_parser.parse_args()

        if args.update:
            upgrade_package()
        elif hasattr(args, 'func'):
            args.func(args)
        else:
            cli_parser.print_help()
            
        # Execute parse_args()
        # args = cli_parser.parse_args()
        # args.func(args)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()