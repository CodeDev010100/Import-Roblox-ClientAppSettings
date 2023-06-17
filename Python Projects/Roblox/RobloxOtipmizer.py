from sys import exit
from time import sleep
from os import linesep
from os.path import exists
from pathlib import Path
from urllib.request import urlopen, urlretrieve
from json import loads

CLIENT_VERSION_JSON = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
STUDIO_VERSION_JSON = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsStudio/channel/zflag").read()

CLIENT_UPLOADED_VERSION = loads(CLIENT_VERSION_JSON)["clientVersionUpload"]
STUDIO_UPLOADED_VERSION = loads(STUDIO_VERSION_JSON)["clientVersionUpload"]

ROBLOX_VERSIONS_FOLDER = Path.home() / 'AppData' / 'Local' / 'Roblox' / 'Versions'

CLIENTAPPSETTINGS_JSON = urlopen("https://raw.githubusercontent.com/L8X/Roblox-Client-Optimizer/main/ClientAppSettings.json").read().decode().rstrip(linesep)

def Import_ClientAppSettings(UPLOADED_VERSION):
    print("[Information] Client version hash: "+ UPLOADED_VERSION)
    VERSION_FOLDER = Path(ROBLOX_VERSIONS_FOLDER) / UPLOADED_VERSION

    if exists(VERSION_FOLDER):
        print("[Sucess] Found \""+VERSION_FOLDER.name+"\" folder!")
        CLIENTSETTINGS_FOLDER = Path(VERSION_FOLDER) / 'ClientSettings'
        if exists(CLIENTSETTINGS_FOLDER):
            print("[Error]: the \""+CLIENTSETTINGS_FOLDER.name+"\" folder has already been inserted")
        else:
            caminho_pasta.mkdir()
            print("[Sucess] \""+CLIENTSETTINGS_FOLDER.name+"\" folder was placed in the folder \""+VERSION_FOLDER.name+"\"")
            json = Path(VERSION_FOLDER) / 'ClientSettings' / 'ClientAppSettings.json'
            json.touch()
            json.write_text(CLIENTAPPSETTINGS_JSON)
            print("[Sucess] ClientAppSettings imported")
            sleep(2)
            exit(0)
    else:
        print("[Error]: Could not find the \""+UPLOADED_VERSION+"\" folder!")
        sleep(2)
        exit(0)
Import_ClientAppSettings(CLIENT_UPLOADED_VERSION) # Put in the parameter the version you want, you can put the client version or the studio version
