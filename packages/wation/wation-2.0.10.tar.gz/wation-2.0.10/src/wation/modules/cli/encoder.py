from ..miscellaneous import file_handler
import os
import base64
import sys
import urllib.parse
import html
import binascii

# Supported encoding algorithms
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
}

def encode_base64(input_data):
    return base64.b64encode(input_data.encode('utf-8')).decode('utf-8')

def encode_base32(input_data):
    return base64.b32encode(input_data.encode('utf-8')).decode('utf-8')

def encode_urlencode(input_data):
    return urllib.parse.quote(input_data)

def encode_fullurlencode(input_data):
    encoded_chars = []
    for char in input_data:
        encoded_chars.append(f"%{ord(char):02X}")
    return ''.join(encoded_chars)

def encode_htmlentity(input_data):
    return html.escape(input_data)

def encode_ascii(input_data):
    return ''.join(chr(ord(c)) if ord(c) < 128 else f"\\u{ord(c):04x}" for c in input_data)

def encode_hex(input_data):
    return binascii.hexlify(input_data.encode('utf-8')).decode('utf-8')

def encode_base16(input_data):
    return base64.b16encode(input_data.encode('utf-8')).decode('utf-8')

def encode_morse(input_data):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }
    return ' '.join(morse_code.get(c.upper(), '') for c in input_data)

def encode_base64url(input_data):
    return base64.urlsafe_b64encode(input_data.encode('utf-8')).decode('utf-8')


def encode_file(file_path, algorithms):
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
        encoded_data = file_bytes
        for algorithm in algorithms:
            if algorithm == 'base64':
                encoded_data = base64.b64encode(encoded_data)
            elif algorithm == 'base32':
                encoded_data = base64.b32encode(encoded_data)
            else:
                raise ValueError(f"Unsupported encoding algorithm: {algorithm}")
        return encoded_data.decode('utf-8')

def calculate_hash(input_data, algorithms):
    encoded_data = input_data
    for algorithm in algorithms:
        if algorithm == 'base64':
            encoded_data = encode_base64(encoded_data)
        elif algorithm == 'base32':
            encoded_data = encode_base32(encoded_data)
        elif algorithm == 'urlencode':
            encoded_data = encode_urlencode(encoded_data)
        elif algorithm == 'fullurlencode':
            encoded_data = encode_fullurlencode(encoded_data)
        elif algorithm == 'htmlentity':
            encoded_data = encode_htmlentity(encoded_data)
        elif algorithm == 'ascii':
            encoded_data = encode_ascii(encoded_data)
        elif algorithm == 'hex':
            encoded_data = encode_hex(encoded_data)
        elif algorithm == 'base16':
            encoded_data = encode_base16(encoded_data)
        elif algorithm == 'morse':
            encoded_data = encode_morse(encoded_data)
        elif algorithm == 'base64url':
            encoded_data = encode_base64url(encoded_data)
        else:
            raise ValueError(f"Unsupported encoding algorithm: {algorithm}")
    
    return encoded_data

def main(args):
    """
    Handle the encode command.

    Args:
        args (Namespace): The parsed arguments.
    """
    try:
        algorithms = args.algorithm.split(',')  # Split algorithms by comma if chaining is specified
        algorithm_names = [algorithm_alias_names.get(algo, algo) for algo in algorithms]

        if os.path.isfile(args.input):
            result = encode_file(args.input, algorithm_names)
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
        if str(e).startswith("Unsupported encoding algorithm:"):
            print(f"[-] Error: Unsupported encoding algorithm '{args.algorithm}'")
        else:
            print(f"[-] Error: {str(e)}")