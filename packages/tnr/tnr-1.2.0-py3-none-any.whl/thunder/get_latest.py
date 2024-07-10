import os
import requests
import urllib.request  # download into memory
import hashlib  # for hashing
import gzip  # for decompressing
import platform  # which OS
import distro  # which linux distribution
from colorama import Fore, Style


# Pulling latest binary from gcs
def get_latest(version: str, path: str) -> str:
    if version != "host" and version != "client":
        return None

    # Validate the platform we're trying to run on
    operating_system = platform.system().lower()
    if version == "host" and operating_system != "windows":
        print(
            Fore.RED
            + "Error: Thunder hosting only supported on Windows machines"
            + Style.RESET_ALL
        )
        exit(1)
    elif version == "client" and operating_system != "linux":
        print(
            Fore.RED
            + "Error: Thunder client only supported on Linux machines"
            + Style.RESET_ALL
        )
        exit(1)

    architecture = platform.machine().lower()
    if operating_system == "linux":
        distribution = distro.id().lower()

    metadata_url = f"https://storage.googleapis.com/storage/v1/b/thunder_binary/o/{version}_{operating_system}_{architecture}?alt=json"
    latest_metadata = requests.get(metadata_url).json().get("metadata")
    if latest_metadata == None:
        print(f"Cannot find latest binary for system {operating_system}/{architecture}")
        return None

    latest_hash = latest_metadata.get("hash")
    if latest_hash == None:
        print(f"Cannot find latest binary for system {operating_system}/{architecture}")
        return None

    # Check if we already have latest binary
    if os.path.isfile(path):
        current_hash = hashlib.md5(open(path, "rb").read()).hexdigest()
        if current_hash == latest_hash:
            return path

    download_url = f"https://storage.googleapis.com/thunder_binary/{version}_{operating_system}_{architecture}"
    compressed_data = urllib.request.urlopen(download_url).read()
    decompressed_data = gzip.decompress(compressed_data)
    
    # Make sure path exists
    if path.startswith('~'):
        path = os.path.expanduser(path)

    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    
    with open(path, "wb") as f:
        f.write(decompressed_data)

    return path
