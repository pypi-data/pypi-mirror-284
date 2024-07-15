import os 
import appdirs
import sys

# App Path
app_path = appdirs.user_data_dir('Wation','Wation')
if not os.path.exists(app_path):
    os.makedirs(app_path)

token_persist_path = os.path.join(app_path, 'token')
client_persist_path = os.path.join(app_path, 'client')

def banner():
    print(f'''
  __     __     ______     ______   __     ______     __   __
 /\ \  _ \ \   /\  __ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \\
 \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \\
  \ \__/".~\_\  \ \_\ \_\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_ \\
   \/_/   \/_/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_/ \/_/
          
    ''')

def clear_terminal():

    # for windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
