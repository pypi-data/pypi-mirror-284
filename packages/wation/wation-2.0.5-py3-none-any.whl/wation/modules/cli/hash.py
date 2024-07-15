from ..miscellaneous import file_handler  # Adjust the import path as per your actual directory structure
import os
import sys
import hashlib
import zlib

# Supported hashing algorithms
SUPPORTED_ALGORITHMS = [
    'md5', 'sha1', 'sha256', 'sha512', 'sha384', 'crc32', 'crc16'
]

algorithm_alias_names = {
    'm': 'md5',
    'md5': 'md5',
    's': 'sha1',
    's1': 'sha1',
    'sha1': 'sha1',
    's256': 'sha256',
    'sha256': 'sha256',
    's512': 'sha512',
    'sha512': 'sha512',
    's384': 'sha384',
    'sha384': 'sha384',
    'crc32': 'crc32',
    'c': 'crc32',
    'c32': 'crc32',
    'crc16': 'crc16',
    'c16': 'crc16',
}

def hash_md5(input_data):
    return hashlib.md5(input_data).hexdigest()

def hash_sha1(input_data):
    return hashlib.sha1(input_data).hexdigest()

def hash_sha256(input_data):
    return hashlib.sha256(input_data).hexdigest()

def hash_sha512(input_data):
    return hashlib.sha512(input_data).hexdigest()

def hash_sha384(input_data):
    return hashlib.sha384(input_data).hexdigest()

def hash_crc32(input_data):
    return format(zlib.crc32(input_data) & 0xFFFFFFFF, '08x')

def hash_crc16(input_data):
    crc = 0xFFFF
    for byte in input_data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return format(crc, '04x')

def hash_data(input_data, algorithms):
    hashed_data = input_data
    for algorithm in algorithms:
        if algorithm == 'md5':
            hashed_data = hash_md5(hashed_data)
        elif algorithm == 'sha1':
            hashed_data = hash_sha1(hashed_data)
        elif algorithm == 'sha256':
            hashed_data = hash_sha256(hashed_data)
        elif algorithm == 'sha512':
            hashed_data = hash_sha512(hashed_data)
        elif algorithm == 'sha384':
            hashed_data = hash_sha384(hashed_data)
        elif algorithm == 'crc32':
            hashed_data = hash_crc32(hashed_data.encode())
        elif algorithm == 'crc16':
            hashed_data = hash_crc16(hashed_data.encode())
        else:
            try:
                hasher = hashlib.new(algorithm)
                hasher.update(hashed_data)
                hashed_data = hasher.hexdigest()
            except ValueError:
                raise ValueError(f"Unsupported hashing algorithm: {algorithm}")
    return hashed_data

def hash_file(file_path, algorithms):
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
        hashed_data = file_bytes
        for algorithm in algorithms:
            if algorithm == 'md5':
                hashed_data = hash_md5(hashed_data)
            elif algorithm == 'sha1':
                hashed_data = hash_sha1(hashed_data)
            elif algorithm == 'sha256':
                hashed_data = hash_sha256(hashed_data)
            elif algorithm == 'sha512':
                hashed_data = hash_sha512(hashed_data)
            elif algorithm == 'sha384':
                hashed_data = hash_sha384(hashed_data)
            elif algorithm == 'crc32':
                hashed_data = hash_crc32(hashed_data)
            elif algorithm == 'crc16':
                hashed_data = hash_crc16(hashed_data)
            else:
                try:
                    hasher = hashlib.new(algorithm)
                    hasher.update(hashed_data)
                    hashed_data = hasher.hexdigest()
                except ValueError:
                    raise ValueError(f"Unsupported hashing algorithm: {algorithm}")
        return hashed_data.decode('utf-8')

def main(args):
    """
    Handle the hash command.

    Args:
        args (Namespace): The parsed arguments.
    """
    try:
        algorithms = args.algorithm.split(',')  # Split algorithms by comma if chaining is specified
        algorithm_names = [algorithm_alias_names.get(algo, algo) for algo in algorithms]

        if os.path.isfile(args.input):
            result = hash_file(args.input, algorithm_names)
        else:
            result = hash_data(args.input.encode('utf-8'), algorithm_names)

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
        if str(e).startswith("Unsupported hashing algorithm:"):
            print(f"[-] Error: Unsupported hashing algorithm '{args.algorithm}'")
        else:
            print(f"[-] Error: {str(e)}")
