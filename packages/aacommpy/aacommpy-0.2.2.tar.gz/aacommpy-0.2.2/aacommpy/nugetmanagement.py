import os
import shutil
import subprocess
import threading
import time
import requests

from aacommpy.dotnetmanagement import copy_nuget_dependencies
from aacommpy.settings import AACOMM_DLL, AACOMMSERVER, AGITO_AACOMM, DEFAULT_NET_FRAMEWORK, NET_FRAMEWORK_CHOICES, NUGET_EXE, NUGET_FOLDER, SYSTEM_IO_PORTS, YAML_DOT_NET, YAML_DOT_NET_40_VER

def dotnetfw(version: str = DEFAULT_NET_FRAMEWORK) -> None:
    if version not in NET_FRAMEWORK_CHOICES:
        raise ValueError(f".NET framework version {version} is not supported.")
    
    latest_version = nuget_version()
    source_dir = os.path.join(os.path.dirname(__file__), NUGET_FOLDER, f"{AGITO_AACOMM}.{latest_version}")
    dest_dir = os.path.dirname(__file__)    
    source_dir = os.path.join(source_dir, 'lib', version)  
    dll_path = os.path.join(source_dir, AACOMM_DLL)
    if not os.path.isfile(dll_path):
        raise FileNotFoundError(f"Could not find {AACOMM_DLL} in {source_dir}.")
    
    shutil.copy2(dll_path, dest_dir)
    print(f"The AAComm .NET target framework is {version}")

    #copy dependencies to the working directory according to the target version
    copy_nuget_dependencies(version, dest_dir)

    return None

def download_nuget_exe() -> None:
    directory = os.path.join(os.path.dirname(__file__), NUGET_FOLDER)
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist

    nuget_path = os.path.join(directory, NUGET_EXE)
    if os.path.exists(nuget_path):
        return None
    
    # Start the progress indicator in a separate thread
    progress_thread = threading.Thread(target=show_progress_indicator, args=(nuget_path,))
    progress_thread.start()

    # Perform the download
    print(f'downloading {NUGET_EXE}...')
    url = f'https://dist.nuget.org/win-x86-commandline/latest/{NUGET_EXE}'
    r = requests.get(url)
    with open(nuget_path, 'wb') as f:
        f.write(r.content)

    # Wait for the progress thread to complete
    progress_thread.join()

    print(f'{NUGET_EXE} downloaded successfully.')
    return None


def show_progress_indicator(nuget_path):
    while not os.path.exists(nuget_path):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('')

def download_aacomm_nuget(version: str = "", update: bool = False) -> None:
    nuget_path = os.path.join(os.path.dirname(__file__), NUGET_FOLDER, NUGET_EXE)
    installed = False
    for dirname in os.listdir(os.path.dirname(nuget_path)):
        if dirname.startswith(f'{AGITO_AACOMM}.') and os.path.isdir(os.path.join(os.path.dirname(nuget_path), dirname)):
            installed = True
            old_version = dirname.split('.')[2:]
            old_version = '.'.join(old_version)
            break
    if update and installed:
        shutil.rmtree(os.path.join(os.path.dirname(nuget_path), f'{AGITO_AACOMM}.{old_version}'))

    # install AAComm nuget
    install_nuget(nuget_path, AGITO_AACOMM, version)

    # install nuget dependency: YamlDotNet 4.2.2 for .NET 4.0
    install_nuget(nuget_path, YAML_DOT_NET, YAML_DOT_NET_40_VER)

    # install nuget dependency: System.IO.Ports 8.0.0 for .NET 6.0 and 8.0
    install_nuget(nuget_path, SYSTEM_IO_PORTS, "")

    # Copy the AACommServer.exe and AACommServerAPI.dll to the working directory
    for dirname in os.listdir(os.path.dirname(nuget_path)):
        if dirname.startswith(f'{AGITO_AACOMM}.') and os.path.isdir(os.path.join(os.path.dirname(nuget_path), dirname)):
            new_version = dirname.split('.')[2:]
            new_version = '.'.join(new_version)
            source_dir = os.path.join(os.path.dirname(nuget_path), f'{AGITO_AACOMM}.{new_version}/build/{AACOMMSERVER}')
            dest_dir = os.path.dirname(__file__)
            shutil.copy2(os.path.join(source_dir, f'{AACOMMSERVER}.exe'), dest_dir)
            shutil.copy2(os.path.join(source_dir, f'{AACOMMSERVER}API.dll'), dest_dir)
            break

    # copy AAComm.dll + dependencies to the working directory        
    dotnetfw()
    return None

def install_nuget(nuget_path, name, version) -> None:
    nuget_cmd = [
    nuget_path,
    'install',
    name,
    '-OutputDirectory', os.path.join(os.path.dirname(nuget_path)),
    '-Source', 'https://api.nuget.org/v3/index.json',
    ]

    if version != "":
        nuget_cmd.extend(['-Version', version])
    else:
        nuget_cmd.extend(['-DependencyVersion', 'Highest']) # Ensure the highest version of dependencies is installed

    subprocess.run(nuget_cmd, check=True)
    return None


def nuget_version() -> str:
    nuget_path = os.path.join(os.path.dirname(__file__), NUGET_FOLDER, NUGET_EXE)
    if not os.path.exists(nuget_path):
        raise RuntimeError("Nuget executable not found. Please run the 'install' command.")
    
    installed = False
    latest_version = None
    for dirname in os.listdir(os.path.dirname(nuget_path)):
        if dirname.startswith(f'{AGITO_AACOMM}.') and os.path.isdir(os.path.join(os.path.dirname(nuget_path), dirname)):
            installed = True
            version = dirname.split('.')[2:]
            latest_version = '.'.join(version)
            print(f"The installed version of {AGITO_AACOMM} is {latest_version}.")
            break

    if not installed:
        raise RuntimeError(f'{AGITO_AACOMM} nuget package is not installed.')
    
    return latest_version

def update_nuget() -> None:
    download_aacomm_nuget(update=True)
    return None