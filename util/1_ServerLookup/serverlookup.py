import requests
from colorama import Fore
from util.plugins.commun import * 

def serverlookup():
    setTitle("Sunucu Bilgileri")
    clear()
    serverlookuptitle()
    print(f"""{y}[{Fore.LIGHTBLUE_EX }#{y}]{w} Bu Bilgileri Alacaksiniz: \n\n""")
    print(f"""          {y}[{w}+{y}]{w} Davet Linki           {y}[{w}+{y}]{w} Davet Eden Kisinin ismi      {y}[{w}+{y}]{w} Sunucu Banneri       {y}[{w}+{y}]{w} Sunucu Banner Fotograf\n""")
    print(f"""          {y}[{w}+{y}]{w} Kanal adi          {y}[{w}+{y}]{w} Davet Eden Kisinin IDsi            {y}[{w}+{y}]{w} Sunucu Aciklamasi     {y}[{w}+{y}]{w} Sunucu Ozellikleri\n""")
    print(f"""          {y}[{w}+{y}]{w} Kanal IDsi            {y}[{w}+{y}]{w} Sunucu Adi            {y}[{w}+{y}]{w} Ozel Davet Linki\n""")
    print(f"""          {y}[{w}+{y}]{w} Gecerlilik Suresi       {y}[{w}+{y}]{w} Sunucu IDsi              {y}[{w}+{y}]{w} Koruma Leveli\n\n\n\n""")
    print(f"{y}[{w}+{y}]{w} Davet Linkini Yapistirin .gg/ dan sonrasi. ")
    invitelink = input(f"""{y}[{b}#{y}]{w} Davet Linki: """)
    clear()
    try:
        res = requests.get(f"https://discord.com/api/v9/invites/{invitelink}")
    except:
        input(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} An error occurred while sending request""")
        main()

    if res.status_code == 200:
        res_json = res.json()

        print(f"""\n{y}[{b}#{y}]{w} Link Bilgileri:""")
        print(f"""          {y}[{w}+{y}]{w} Davet Linki: {f'https://discord.gg/{res_json["code"]}'}""")
        print(f"""          {y}[{w}+{y}]{w} Kanal: {res_json["channel"]["name"]} ({res_json["channel"]["id"]})""")
        print(f"""          {y}[{w}+{y}]{w} Gecerlilik Suresi: {res_json["expires_at"]}\n""")

        print(f"""{y}[{b}#{y}]{w} Davet Eden Kisinin Bilgileri:""")
        print(f"""          {y}[{w}+{y}]{w} Isim: {f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'}""")
        print(f"""          {y}[{w}+{y}]{w} Kullanici ID: {res_json["inviter"]["id"]}\n""")

        print(f"""{y}[{b}#{y}]{w} Sunucu Bigileri:""")
        print(f"""          {y}[{w}+{y}]{w} Isim: {res_json["guild"]["name"]}""")
        print(f"""          {y}[{w}+{y}]{w} Sunucu ID: {res_json["guild"]["id"]}""")
        print(f"""          {y}[{w}+{y}]{w} Banner: {res_json["guild"]["banner"]}""")
        print(f"""          {y}[{w}+{y}]{w} Aciklama: {res_json["guild"]["description"]}""")
        print(f"""          {y}[{w}+{y}]{w} Ozel Baglanti: {res_json["guild"]["vanity_url_code"]}""")
        print(f"""          {y}[{w}+{y}]{w} Koruma Leveli: {res_json["guild"]["verification_level"]}""")
        print(f"""          {y}[{w}+{y}]{w} Splash: {res_json["guild"]["splash"]}""")
        print(f"""          {y}[{w}+{y}]{w} Ozellikleri: {res_json["guild"]["features"]}""")
    else:
        input(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} An error occurred while sending request""")
        main()
    
    input(f"""\n\n{y}[{b}#{y}]{w} Cikmak icin ENTER bas""")
    main()

serverlookup()
