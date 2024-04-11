import requests
import time
from colorama import Fore
import threading
from util.plugins.commun import * 

def webhookspam():
    setTitle("WebHook Spammer")
    clear()
    webhspamtitle()
    print(f"{y}[{w}+{y}]{w} Spam Atmak Istediginiz Webhook Linkini Girin ")
    webhook = input(f"{y}[{b}#{y}]{w} WebHook Link: ")
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print(f"      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Webhook Linki Yanlis !")
        time.sleep(2)
        clear()
        main()
    print(f"\n{y}[{w}+{y}]{w} Spam Atilacak Mesaji Yazin ")
    message = input(f"{y}[{b}#{y}]{w} Mesaj: ")
    print(f"\n{y}[{w}+{y}]{w} Kac Tane Gonderilecek ")
    amount = int(input(f"{y}[{b}#{y}]{w} Kac tane: "))
    def spam():
        requests.post(webhook, json={'content': message})
    for x in range(amount):
        threading.Thread(target = spam).start()
    
    clear()
    webhspamtitle()
    print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Webhook Mesajlari Gonderdi")
    input(f"\n{y}[{b}#{y}]{w} Cikmak Icin Enter Basin")
    main()

webhookspam()
