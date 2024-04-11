import os, os.path
from colorama import Fore
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from utili import *

### SETUP DISCORD ###
import nextcord
from nextcord.errors import LoginFailure
from nextcord.ext import commands
from nextcord.utils import get
from nextcord.errors import Forbidden
intents = nextcord.Intents.default()
intents.members = True
intents.guild_messages = True 
intents.messages = True
intents.guilds = True
nuker = commands.Bot(command_prefix=";",intents=intents)

impostatitolo(f"ErencanDeniz Patlatma Araci {VERSIONETOOL} - Sunucu adi Degistirme")
clear()
filetoken = open("token.txt", "r")
token = filetoken.read()

@nuker.event
async def on_ready():
    clear()
    fileserver = open("server.txt", "r")
    server = fileserver.read()
    serverr = nuker.get_guild(int(server))
    print(F"{m}Bot Basariyla Giris Yapti:" + f'{w}')
    print(f"{m}ID: " + str(nuker.user.id) + f'{w}')
    print(f"{m}Kullanici adi: " + str(nuker.user.name) + f'{w}')
    print(f"{m}Sunucu ID: " + server + f'{w}')
    try:
        await serverr.edit(name="PATLATILDI | ErencanDeniz Araci [itempazar.com/erencandeniz]", community=False)
        print(f'{y}[{b}ErencanDeniz{y}]{g} Sunucu adini degistirdim{w}')
    except Forbidden:
        print(f'{y}[{b}ErencanDeniz{y}]{r} Sunucu adini degistiremedim [Izin yok]{w}')
    except:
        print(f'{y}[{b}ErencanDeniz{y}]{r} Sunucu adini degistiremedim{w}')


nuker.run(token)