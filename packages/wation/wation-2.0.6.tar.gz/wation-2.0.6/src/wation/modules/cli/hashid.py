import re
import base64
import urllib.parse

hash_type_map = {
    'MD5': re.compile(r'^[a-f0-9]{32}$', re.IGNORECASE),
    'SHA1': re.compile(r'^[a-f0-9]{40}$', re.IGNORECASE),
    'SHA224': re.compile(r'^[a-f0-9]{56}$', re.IGNORECASE),
    'SHA256': re.compile(r'^[a-f0-9]{64}$', re.IGNORECASE),
    'SHA384': re.compile(r'^[a-f0-9]{96}$', re.IGNORECASE),
    'SHA512': re.compile(r'^[a-f0-9]{128}$', re.IGNORECASE),
    'CRC16': re.compile(r'^[a-f0-9]{4}$', re.IGNORECASE),
    'CRC32': re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE),
    'DES': re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE),
    'UUIDv1': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-1[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE),
    'UUIDv2': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-2[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE),
    'UUIDv3': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-3[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE),
    'UUIDv4': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE),
    'UUIDv5': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-5[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE),
    'MD5Crypt': re.compile(r'^\$1\$[a-zA-Z0-9./]{0,8}\$[a-zA-Z0-9./]{22}$'),
    'SHA256Crypt': re.compile(r'^\$5\$[a-zA-Z0-9./]{0,16}\$[a-zA-Z0-9./]{43}$'),
    'SHA512Crypt': re.compile(r'^\$6\$[a-zA-Z0-9./]{0,16}\$[a-zA-Z0-9./]{86}$'),
    'BCrypt': re.compile(r'^\$2[aby]\$\d{2}\$[./a-zA-Z0-9]{53}$'),
    'NTLM': re.compile(r'^([a-f0-9]{32}|[a-f0-9]{48})$', re.IGNORECASE)
}

def detect_hash_type(hash_str):
    hash_str = urllib.parse.unquote(hash_str)
    for hash_type, regex in hash_type_map.items():
        if regex.match(hash_str):
            return hash_type

    try:
        base64.b64decode(hash_str, validate=True)
        if re.match(r'.*\={1,2}$', hash_str):
            return 'BASE64'
        else:
            return 'BASE64 (50%)'
    except Exception:
        return None
    
def main(args):
    hash_str = args.input
    hash_type = detect_hash_type(hash_str)

    if hash_type:
        print(f"[+] Detected hash/encoding type: {hash_type}")
    else:
        print("[-] Could not determine the hash/encoding type")
