
### IMPORT ###
import os
import requests, os, sys, re, time, os.path, ctypes, getpass
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore
from urllib.request import Request, urlopen
import nextcord

### RENKLER ###
VERSIONETOOL = "0.0.1 [BETA]"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX


### DISCORDU INDIR ###
import nextcord
from nextcord.errors import LoginFailure
from nextcord.ext import commands
from nextcord.utils import get
intents = nextcord.Intents.default()
intents.members = True
intents.guild_messages = True 
intents.messages = True
intents.guilds = True
#nuker = commands.Bot(command_prefix=";",intents=intents)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

nuker = Bot()


global statobot
statobot = 'CevrimDisi'

### EKRAN ###
def impostatitolo(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | itempazar.com/ErencanDeniz")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | itempazar.com/ErencanDeniz\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def titolohome():
#    print(f"""\n\n
#             
#          ███████╗██████╗░███████╗███╗░░██╗░█████╗░░█████╗░███╗░░██╗██████╗░███████╗███╗░░██╗██╗███████╗
#          ██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔════╝████╗░██║██║╚════██║
#          █████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝███████║██╔██╗██║██║░░██║█████╗░░██╔██╗██║██║░░███╔═╝
#          ██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██╔══██║██║╚████║██║░░██║██╔══╝░░██║╚████║██║██╔══╝░░
#          ███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║░░██║██║░╚███║██████╔╝███████╗██║░╚███║██║███████╗
#          ╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚══════╝                 
                  
#\n""".replace('█', f'{g}█{y}'))
    print(f"""\n\n
                                 
███████╗██████╗░███████╗███╗░░██╗░█████╗░░█████╗░███╗░░██╗
██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██╔══██╗████╗░██║
█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝███████║██╔██╗██║
██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██╔══██║██║╚████║
███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║░░██║██║░╚███║
╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝

██████╗░░█████╗░████████╗██╗░░░░░░█████╗░████████╗███╗░░░███╗░█████╗░  ░█████╗░██████╗░░█████╗░░█████╗░██╗
██╔══██╗██╔══██╗╚══██╔══╝██║░░░░░██╔══██╗╚══██╔══╝████╗░████║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
██████╔╝███████║░░░██║░░░██║░░░░░███████║░░░██║░░░██╔████╔██║███████║  ███████║██████╔╝███████║██║░░╚═╝██║
██╔═══╝░██╔══██║░░░██║░░░██║░░░░░██╔══██║░░░██║░░░██║╚██╔╝██║██╔══██║  ██╔══██║██╔══██╗██╔══██║██║░░██╗██║
██║░░░░░██║░░██║░░░██║░░░███████╗██║░░██║░░░██║░░░██║░╚═╝░██║██║░░██║  ██║░░██║██║░░██║██║░░██║╚█████╔╝██║
╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝
\n""".replace('█', f'{g}█{y}'))

banner = r"""
██╗░░░██╗██╗░░░██╗██╗░░██╗██╗░░░░░███████╗███╗░░██╗██╗██╗░░░██╗░█████╗░██████╗░
╚██╗░██╔╝██║░░░██║██║░██╔╝██║░░░░░██╔════╝████╗░██║██║╚██╗░██╔╝██╔══██╗██╔══██╗
░╚████╔╝░██║░░░██║█████═╝░██║░░░░░█████╗░░██╔██╗██║██║░╚████╔╝░██║░░██║██████╔╝
░░╚██╔╝░░██║░░░██║██╔═██╗░██║░░░░░██╔══╝░░██║╚████║██║░░╚██╔╝░░██║░░██║██╔══██╗
░░░██║░░░╚██████╔╝██║░╚██╗███████╗███████╗██║░╚███║██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
"""[1:]

def transizione():
    clear()
    caricamento()
    clear()

def caricamento():
	carattere = ['|', '/', '-', '\\']
	for i in carattere+carattere+carattere:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Yukleniyor... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

@nuker.event
async def on_ready():
    global statobot
    statobot = 'Cevrimici'
    print("Bot Girisi:")
    print("ID: " + str(nuker.user.id))
    print("Isim: " + str(nuker.user.name))
    main()

from scripts import *
def main():
    impostatitolo(f"Erencan Patlatma Aleti {VERSIONETOOL} - Yukleniyor")
    System.Size(160, 40) #120, 30
    Anime.Fade(Center.Center(banner), Colors.green_to_red, Colorate.Vertical, time=1)
    clear()
    try:
        filetoken = open("token.txt", "r")
        token = 'Bulundu'
    except:
        token = 'Bulunamadi'
    try:
        fileserver = open("server.txt", "r")
        server = fileserver.read()
    except:
        server = 'Bulunamadi'
    global statobot
    impostatitolo(f"ErencanDeniz Patlatma Araci {VERSIONETOOL}")
    titolohome()
    print(f"""      {y}[{b}+{y}]{g} Main:                                                                     {y}[{b}+{y}]{c} Ayarlar:
          {y}[{w}1{y}]{g} Tum kullanicilari yasakla                                                  {y}[{w}10{y}]{c} Botun Tokeni
          {y}[{w}2{y}]{g} Tum kanallari sil                                                          {y}[{w}11{y}]{c} Sunucu IDsi              
          {y}[{w}3{y}]{g} Tum rolleri sil                                                            {y}[{w}12{y}]{c} Botu baslat 
          {y}[{w}4{y}]{g} Herkese yonetici rolu ver
          {y}[{w}5{y}]{g} Kanal olustur
          {y}[{w}6{y}]{g} Sunucunun adini degistir
          {y}[{w}7{y}]{g} Sunucudaki emojileri sil

                                                                                     {m}ErencanDeniz tarafindan yapildi | itempazar.com/ErencanDeniz
                                                                                     {m}Token     : {b}{token}
                                                                                     {m}Server    : {b}{server}
                                                                                     {m}Bot Durumu: {b}{statobot}
\t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global scelta
    scelta = input(f"""{y}[{b}#{y}]{w} [{getpass.getuser()}]: """)
    if scelta == '1' or scelta == '01':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/1_BanAll.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '2' or scelta == '02':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/2_EliminaCanali.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '3' or scelta == '03':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/3_EliminaRuoli.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '4' or scelta == '04':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/4_ModificaEveryone.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '5' or scelta == '05':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/5_CreaCanali.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '6' or scelta == '06':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/6_CambiaNomeServer.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '7' or scelta == '07':
        if statobot == 'Cevrimici':
            try:
                fileserver = open("server.txt", "r")
                server = fileserver.read()
                serverr = nuker.get_guild(int(server))
                os.system('python ./scripts/7_EliminaEmoji.py')
            except FileNotFoundError:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Sunucu IDsi eksik [Ayarlarda 11. Secenek]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Botu baslat [Ayarlarda 12. Secenek]!")
            main()
    elif scelta == '10' or scelta == '010':
        transizione()
        diocane = input(f'{y}[{b}#{y}]{w} Bot tokeninizi girin:    ')
        file = open(f"token.txt", 'w')
        file.write(f"{diocane}")
        file.close()
        main()
    elif scelta == '11' or scelta == '011':
        transizione()
        diocane = input(f'''{y}[{b}#{y}]{w} Patlatalacak sunucunun IDsini girin:    ''')
        file = open(f"server.txt", 'w')
        file.write(f"{diocane}")
        file.close()
        main()
    elif scelta == '12' or scelta == '012':
        transizione()
        try:
            filetoken = open("token.txt", "r")
            token = filetoken.read()
            try:
                nuker.run(f'{token}')
            except LoginFailure:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Girilen ID Gecersiz!")
        except Exception as errore:
            print(errore)
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Oncelikle bot tokenini ve IDyi yapmaniz gerek!")
            main()
    elif scelta == 'exit' or scelta == 'chiudi':
        transizione()
        sys.exit()
    else:
        clear()
        main()




main()
