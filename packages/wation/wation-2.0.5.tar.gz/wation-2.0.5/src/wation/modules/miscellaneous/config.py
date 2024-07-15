import os
import json
from cryptography.fernet import Fernet
from wation.modules.cli.general import app_path

# Paths for the key and config files
key_file_path = os.path.join(app_path, 'junk.tmp')
config_file_path = os.path.join(app_path, 'cache.tmp')

def _ensure_directory():
    """Ensure the application directory exists."""
    if not os.path.exists(app_path):
        os.makedirs(app_path)

def _load_key():
    """Load the encryption key from file or generate a new one if it doesn't exist."""
    _ensure_directory()
    if os.path.exists(key_file_path):
        with open(key_file_path, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file_path, 'wb') as f:
            f.write(key)
        return key

def _encrypt(data, key):
    """Encrypt the given data using the provided key."""
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def _decrypt(encrypted_data, key):
    """Decrypt the given data using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

def _load_config():
    """Load and decrypt the config file if it exists, otherwise return an empty dictionary."""
    if os.path.exists(config_file_path):
        with open(config_file_path, 'rb') as f:
            encrypted_data = f.read()
            key = _load_key()
            decrypted_data = _decrypt(encrypted_data, key)
            return json.loads(decrypted_data)
    return {}

def _save_config(config):
    """Encrypt and save the config dictionary to the config file."""
    key = _load_key()
    encrypted_data = _encrypt(json.dumps(config), key)
    with open(config_file_path, 'wb') as f:
        f.write(encrypted_data)

def set(config_name, config_value):
    """Set a configuration value."""
    config = _load_config()
    config[config_name] = config_value
    _save_config(config)

def get(config_name):
    """Get a configuration value."""
    config = _load_config()
    return config.get(config_name, None)

def unset(config_name):
    """Remove a configuration value."""
    config = _load_config()
    if config_name in config:
        del config[config_name]
        _save_config(config)

def set_items(items):
    """Set multiple configuration values at once.
    
    Args:
        items (dict): Dictionary of config_name: config_value pairs to set.
    """
    config = _load_config()
    config.update(items)
    _save_config(config)

def unset_items(keys):
    """Unset multiple configuration values at once.
    
    Args:
        keys (list): List of config_names to remove.
    """
    config = _load_config()
    for key in keys:
        if key in config:
            del config[key]
    _save_config(config)

def reset_config():
    """Remove the key file and config file to reset all configurations."""
    if os.path.exists(key_file_path):
        os.remove(key_file_path)
    if os.path.exists(config_file_path):
        os.remove(config_file_path)