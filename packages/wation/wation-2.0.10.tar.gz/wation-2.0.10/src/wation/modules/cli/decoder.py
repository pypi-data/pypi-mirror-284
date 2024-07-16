from ..miscellaneous import file_handler  # Adjust the import path as per your actual directory structure
import os
import base64
import sys
import urllib.parse
import html
import binascii
import json 

# Supported decoding algorithms
SUPPORTED_ALGORITHMS = [
    'base64', 'base32', 'base16', 'urlencode', 'fullurlencode', 'htmlentity', 
    'ascii', 'hex', 'morse', 'base64url'
]

algorithm_alias_names = {
    'b64': 'base64',
    'b': 'base64',
    'b32': 'base32',
    'u': 'urlencode',
    'uf': 'fullurlencode',
    'he': 'htmlentity',
    'a': 'ascii',
    'h': 'hex',
    'b16': 'base16',
    'm': 'morse',
    'b64u': 'base64url',
    'jwt': 'jwt'
}

def decode_base64(input_data):
    return base64.b64decode(input_data.encode('utf-8')).decode('utf-8')

def decode_base32(input_data):
    return base64.b32decode(input_data.encode('utf-8')).decode('utf-8')

def decode_urlencode(input_data):
    return urllib.parse.unquote(input_data)

def decode_fullurlencode(input_data):
    bytes_data = bytearray()
    input_data = input_data.replace('%', '')
    for i in range(0, len(input_data), 2):
        bytes_data.append(int(input_data[i:i+2], 16))
    return bytes_data.decode('utf-8')

def decode_htmlentity(input_data):
    return html.unescape(input_data)

def decode_ascii(input_data):
    return input_data.encode('utf-8').decode('unicode_escape')

def decode_hex(input_data):
    return binascii.unhexlify(input_data.encode('utf-8')).decode('utf-8')

def decode_base16(input_data):
    return base64.b16decode(input_data.encode('utf-8')).decode('utf-8')

def decode_morse(input_data):
    morse_code = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
    }
    return ''.join(morse_code.get(char, '') for char in input_data.split(' '))

def decode_base64url(input_data):
    return base64.urlsafe_b64decode(input_data.encode('utf-8')).decode('utf-8')

def decode_file(file_path, algorithms):
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
        decoded_data = file_bytes
        for algorithm in algorithms:
            if algorithm == 'base64':
                decoded_data = base64.b64decode(decoded_data)
            elif algorithm == 'base32':
                decoded_data = base64.b32decode(decoded_data)
            else:
                raise ValueError(f"Unsupported decoding algorithm: {algorithm}")
        return decoded_data.decode('utf-8')

def add_padding(input_data):
    # Calculate the required padding
    padding = '=' * ((4 - len(input_data) % 4) % 4)
    return input_data + padding

def decode_jwt(input_data):
    try:
        header, payload, signature = input_data.split('.')
        decoded_header = decode_base64url(add_padding(header))
        decoded_payload = decode_base64url(add_padding(payload))
        return f"\n\nHeader: {json.dumps(json.loads(decoded_header), indent=2)}\nPayload: {json.dumps(json.loads(decoded_payload), indent=2)}"
    except Exception as e:
        raise ValueError(f"Failed to decode JWT: {str(e)}")

def calculate_hash(input_data, algorithms):
    decoded_data = input_data
    for algorithm in algorithms:
        if algorithm == 'base64':
            decoded_data = decode_base64(decoded_data)
        elif algorithm == 'base32':
            decoded_data = decode_base32(decoded_data)
        elif algorithm == 'urlencode':
            decoded_data = decode_urlencode(decoded_data)
        elif algorithm == 'fullurlencode':
            decoded_data = decode_fullurlencode(decoded_data)
        elif algorithm == 'htmlentity':
            decoded_data = decode_htmlentity(decoded_data)
        elif algorithm == 'ascii':
            decoded_data = decode_ascii(decoded_data)
        elif algorithm == 'hex':
            decoded_data = decode_hex(decoded_data)
        elif algorithm == 'base16':
            decoded_data = decode_base16(decoded_data)
        elif algorithm == 'morse':
            decoded_data = decode_morse(decoded_data)
        elif algorithm == 'base64url':
            decoded_data = decode_base64url(decoded_data)
        elif algorithm == 'jwt':
            decoded_data = decode_jwt(decoded_data)
        else:
            raise ValueError(f"Unsupported decoding algorithm: {algorithm}")
    
    return decoded_data

def main(args):
    """
    Handle the decode command.

    Args:
        args (Namespace): The parsed arguments.
    """
    try:
        algorithms = args.algorithm.split(',')  # Split algorithms by comma if chaining is specified
        algorithm_names = [algorithm_alias_names.get(algo, algo) for algo in algorithms]

        if os.path.isfile(args.input):
            result = decode_file(args.input, algorithm_names)
        else:
            result = calculate_hash(args.input, algorithm_names)

        if args.output:
            file_handler.save(result, args.output)
            print(f"[+] Output saved to: {args.output}")
        else:
            if sys.stdout.isatty():
                alg_names = ",".join(algorithm_names).capitalize()
                print(f"[+] Input value: {args.input}")
                print(f"[+] {alg_names} value: {result}")
            else:
                sys.stdout.write(result + '\n')
                
    except ValueError as e:
        if str(e).startswith("Unsupported decoding algorithm:"):
            print(f"[-] Error: Unsupported decoding algorithm '{args.algorithm}'")
        else:
            print(f"[-] Error: {str(e)}")