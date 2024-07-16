import threading
import time
import sys
from .general import banner, clear_terminal
from wation import collaborator
from wation import Wation

# Event to signal when logs are retrieved
logs_received_event = threading.Event()

def inner_banner():
    
    clear_terminal()  # Clear the console screen
    banner()
    print(f"[~] Endpoint url: {endpoint}")

def print_output():
    global logs_received_event

    inner_banner()
    print("[~] Listening for incoming requests ...")

    while True:
        try:
            logs = collaborator.requests_logs()

            for log in logs:
                print(
                    f"Protocol: {log['protocol']}",
                    f"Requested at: {log['requested_at']['date']} {log['requested_at']['time']}",
                    f"Client: {log['client']['ip']}:{log['client']['port']}",
                sep="\n")

                print(f"\nRequest:\n")
                if log['protocol'] == "http":
                    request = log['http']['request'].replace("\r\n\r\n", "")
                    print(f"{request}")
                if log['protocol'] == "dns":
                    print(f"Type: {log['dns']['request']['type']['label']}")
                    print(f"{log['dns']['request']['domain']}")

                print('-'*10)

            if logs:
                logs_received_event.set()  # Set the event if logs are retrieved

            time.sleep(10)
        except Exception as e:
            print(f'[-] {e}')
            logs_received_event.set()

def main(args):
    global endpoint, wation

    wation = Wation.instance()

    if not args.keep_requests:
        collaborator.enpoint_refresh()

    # wation.collaborator_enpoint_refresh()
    try:
        endpoint = collaborator.enpoint_request()
    except ValueError as e:
        sys.exit(f'[-] {e}')
    
    collab_thread = threading.Thread(target=print_output)
    collab_thread.daemon = True
    collab_thread.start()

    start_time = time.time()
    timeout = 600  # 10 minutes timeout
    
    try:
        while not logs_received_event.is_set():
            if time.time() - start_time > timeout:
                print("\nTimeout reached. Exiting...")
                break
            time.sleep(0.1)  # Keep the main thread alive until logs are received
            
        print("\nRequests received. Exiting...")
    except KeyboardInterrupt:
        print("\nCollaborator terminated.")