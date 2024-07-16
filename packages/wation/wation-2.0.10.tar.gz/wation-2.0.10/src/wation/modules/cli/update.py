import subprocess
import sys
from wation import Wation
from ..miscellaneous import server

def update_package():
    package_name = "wation"  # Replace with your package name
    try:
        # Run the pip install command to upgrade the package
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
        print(f"Package '{package_name}' upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade package '{package_name}'. Error: {e}")