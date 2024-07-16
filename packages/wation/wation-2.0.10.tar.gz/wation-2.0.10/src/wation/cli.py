#!/usr/bin/env python3

import argparse
import sys
import time

from wation.modules.cli.encoder import main as cli_encoder_handler
from wation.modules.cli.encoder import SUPPORTED_ALGORITHMS as ENCODER_SUPPORTED_ALGORITHMS

from wation.modules.cli.decoder import main as cli_decoder_handler
from wation.modules.cli.decoder import SUPPORTED_ALGORITHMS as DECODER_SUPPORTED_ALGORITHMS

from wation.modules.cli.hash import main as cli_hash_handler
from wation.modules.cli.hash import SUPPORTED_ALGORITHMS as HASH_SUPPORTED_ALGORITHMS

from wation.modules.cli.uuid import main as cli_uuid_handler
from wation.modules.cli.hashid import main as cli_hashid_handler
from wation.modules.cli.collab import main as cli_collab_handler

from wation.modules.cli.general import banner, clear_terminal

from wation.modules.cli.auth import arg_login, arg_logout
from wation.modules.cli.open import arg_open
from wation.modules.cli.connection import arg_connection
from wation.modules.cli.profile import arg_profile
from wation.modules.cli.update import update_package
from wation.modules.miscellaneous import config
from wation.modules.miscellaneous import server
from wation import Wation

def main():

    try:
        if sys.stdout.isatty():
            clear_terminal()
            banner()

        # parser
        cli_parser = argparse.ArgumentParser(prog='wation', description='Wation CLI Connector.')
        cli_parser.add_argument("--version", "-v", action="version", version=f"[+] Version: v{Wation.module_version}", help="Show version information")
        cli_parser.add_argument("--update", "-u", action="store_true", help="Upgrade the package")
        
        cli_subparsers = cli_parser.add_subparsers(title="subcommands", dest="command", help="Available commands")

        client_id = config.get("client_id")
        if client_id:

            current_time = time.time()
            # Calculate the difference in seconds
            time_difference = True
            if config.get("last_sync"):
                time_difference = current_time - config.get("last_sync")

            # Check if more than 24 hours (86400 seconds) have passed
            if time_difference == True or time_difference > 86400:
                print('[~] Syncing wation profile...')
                server.sync_config()
            
            features = config.get('features')

            if 'encode' in features:
                hash_command = cli_subparsers.add_parser('hash', help="Hash a string or file.")
                hash_command.add_argument("input", type=str, help="String or path to the file to hash.")
                hash_command.add_argument('-a', '--algorithm', type=str, default='md5', 
                                        help=f"The hashing algorithm to use. Supported algorithms: {', '.join(HASH_SUPPORTED_ALGORITHMS)}.")
                hash_command.add_argument("--output", "-o", type=str, help="Path to save the output. If not provided, prints the result.")
                hash_command.set_defaults(func=cli_hash_handler)

                encode_command = cli_subparsers.add_parser('encode', help="Encode a string or file.")
                encode_command.add_argument("input", type=str, help="String or path to the file to encode.")
                encode_command.add_argument('-a', '--algorithm', type=str, default='base64', 
                    help=f"The algorithm(s) to use for encoding. Supported algorithms: {', '.join(ENCODER_SUPPORTED_ALGORITHMS)}. Multiple algorithms should be comma-separated.")
                encode_command.add_argument("--output", "-o", type=str, help="Path to save the output. If not provided, prints the result.")
                encode_command.set_defaults(func=cli_encoder_handler)

            if 'decode' in features:
                decode_command = cli_subparsers.add_parser('decode', help="Decode a string or file.")
                decode_command.add_argument("input", type=str, help="String or path to the file to decode.")
                decode_command.add_argument('-a', '--algorithm', type=str, default='base64', 
                                            help=f"The algorithm(s) to use for decoding. Supported algorithms: {', '.join(DECODER_SUPPORTED_ALGORITHMS)}. Multiple algorithms should be comma-separated.")
                decode_command.add_argument("--output", "-o", type=str, help="Path to save the output. If not provided, prints the result.")
                decode_command.set_defaults(func=cli_decoder_handler)

            # Hash ID command
            if 'hashid' in features:
                hashid_command = cli_subparsers.add_parser('hashid', help="Detect the hash or encoding type of a given string.")
                hashid_command.add_argument("input", type=str, help="The string to detect the hash or encoding type.")
                hashid_command.set_defaults(func=cli_hashid_handler)
            
            # collab command
            if 'collab' in features:
                collab_command = cli_subparsers.add_parser('collab', help="Initialize the Collaborator Endpoint to listen for incoming requests, supporting both DNS and HTTP/S protocols.")
                collab_command.add_argument('-k', '--keep-requests', action='store_true', help="Keep using the previous endpoint and retain previous requests.")
                collab_command.set_defaults(func=cli_collab_handler)

            # UUID command
            if 'uuid' in features:
                uuid_command = cli_subparsers.add_parser('uuid', help="Generate UUIDs, supporting versions 1, 3, 4, and 5.")
                uuid_command.add_argument('-v', '--version', type=int, default=4, choices=[1, 3, 4, 5],
                                        help="UUID version (default: 4).")
                uuid_command.add_argument('-n', '--namespace', type=str,
                                        help="Namespace for UUID version 3 or 5.")
                uuid_command.add_argument('-q', '--quantity', type=int, default=1,
                                        help="Quantity of UUIDs to generate (default: 1).")
                uuid_command.add_argument('-o', '--output', type=str,
                                        help="Path to save the UUIDs. If not provided, prints the result.")
                uuid_command.set_defaults(func=cli_uuid_handler)

            profile_command = cli_subparsers.add_parser('profile', help="Show your profile information.")
            profile_command.set_defaults(func=arg_profile)

        connection_command = cli_subparsers.add_parser('connection', help="Checks your internet connection and the accessibility of Wation.")
        connection_command.set_defaults(func=arg_connection)

        open_command = cli_subparsers.add_parser('open', help="Open Wation.net in the default browser.", description="Open Wation.net in the default browser.")
        open_command.set_defaults(func=arg_open)

        if client_id:
            logout_command = cli_subparsers.add_parser('logout', help="Log out of your current Wation session.")
            logout_command.set_defaults(func=arg_logout)
        else:
            login_command = cli_subparsers.add_parser('login', help="Log in to Wation using your credentials.")
            login_command.set_defaults(func=arg_login)

        # if len(sys.argv) <= 1:
        #     sys.argv.append('--help')

        args = cli_parser.parse_args()

        if args.update:
            update_package()
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