from sys import exit
from time import sleep
from os import getenv, linesep, system
from os.path import exists
from pathlib import Path
from urllib.request import urlopen, urlretrieve
from json import loads
import shutil

CLIENT_VERSION_JSON = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
CLIENT_VERSION = loads(CLIENT_VERSION_JSON)["clientVersionUpload"]

ROBLOX_VERSIONS_FOLDER = Path.home() / 'AppData' / 'Local' / 'Roblox' / 'Versions'
ROBLOX_VERSION_FOLDER = None

print("Client version hash: "+CLIENT_VERSION)

CLIENTAPPSETTINGS_JSON = urlopen("https://raw.githubusercontent.com/L8X/Roblox-Client-Optimizer/main/assets/ClientAppSettings.json").read().decode().rstrip(linesep)

if exists(ROBLOX_VERSIONS_FOLDER):
    ROBLOX_VERSION_FOLDER = Path(ROBLOX_VERSIONS_FOLDER) / CLIENT_VERSION
    print("Found \""+ROBLOX_VERSION_FOLDER.name+"\" folder!")
else:
    print("[Error]: Could not find the \""+ROBLOX_VERSION_FOLDER.name+"\" folder!")
    exit(1)

caminho_pasta = Path(ROBLOX_VERSION_FOLDER) / 'ClientSettings'
caminho_pasta.mkdir()
json = Path(ROBLOX_VERSION_FOLDER) / 'ClientSettings' / 'ClientAppSettings.json'
json.touch()
json.write_text(CLIENTAPPSETTINGS_JSON)

for _ in range(3,0,-1):
    system("title "+"Closing in "+_.__str__())
    print('.')
    sleep(1)
exit(0)