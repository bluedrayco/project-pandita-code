from lcd.catalog import Catalog
from mp3.playlist import Playlist,PlaylistConfig
from httpclient import HttpClient
import network   # importa el módulo network
import time
import machine
import json
import gc


def getRepoConfig(client:HttpClient,repoURL:str)->dict:
    configUrl = f"{repoURL}/config.json"
    print(configUrl)
    #client.request("GET",configUrl,saveToFile="config.json")
    with open("config.json") as f:
        content = f.read()
    config = json.loads(content)
    return config

def getInternalConfig()->dict:
    with open("internal_config.json") as f:
        content = f.read()
    return json.loads(content)

def connectToSSID(SSID:str,PASSWORD:str):
    print(f"Connecting to {SSID}...")
    sta_if = network.WLAN(network.STA_IF)
    time.sleep_ms(300)
    sta_if.active(False) 
    time.sleep_ms(300)
    sta_if.active(True)
    time.sleep_ms(300)
    sta_if.scan()
    time.sleep_ms(1000)
    sta_if.connect(SSID, PASSWORD)
    time.sleep_ms(5000)
    print(sta_if.isconnected())

    
try:
    config = getInternalConfig()
    print(config)
    #connectToSSID(config['modem_ssid'],config['modem_password'])
    print("hola mundo!!!")
    http = HttpClient()
    repoConfig = getRepoConfig(http,config['repoURL'])
    print(repoConfig)
    print("termine")
    #playlist = Playlist(PlaylistConfig("songs",config['volume'],repoConfig['mp3']['start'],repoConfig['mp3']['end'],repoConfig['mp3']['exclude']))
    #playlist.runFirst()
    catalog = Catalog(http,"",1,2)
    #catalog = Catalog(http,config['repoURL'],repoConfig['images']['fotos']['start'],repoConfig['images']['fotos']['end'],repoConfig['images']['fotos']['exclude'])
    catalog.printImage()
    gc.collect()
except Exception as e:
    print("----")
    print(e)
    print("----")
