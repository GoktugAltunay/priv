from util.plugins.update import search_for_updates
from util.plugins.commun import *

def main():
    clear()
    setTitle(f"ErencanDeniz v{THIS_VERSION}")
    astraahometitle()
    print(f"""{y}[{b}+{y}]{w} Seçenekler:
  
{y}[{w}1{y}]{w} Sunucu Bilgileri
{y}[{w}2{y}]{w} Token Bilgileri    
{y}[{w}3{y}]{w} Mass DM
{y}[{w}4{y}]{w} Webhook Spammer
{y}[{w}5{y}]{w} Token BruteForce
{y}[{w}6{y}]{w} Thread Spammer
\t\t\t\t\t\t\t\t\t\t\t\t {y}[{b}>{y}]{w}Sonraki Sayfa""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Seçiminiz: """).lstrip("0")
    
    
    if choice == '1':
        transition()
        exec(open('util/1_ServerLookup/serverlookup.py').read())
    elif choice == '2':
        transition()
        exec(open('util/2_TokenInfo/tokeninfo.py').read())
    elif choice == '3':
        transition()
        exec(open('util/3_MassDM/massdm.py').read())
    elif choice == '4':
        transition()
        exec(open('util/4_WebHSpam/webhspam.py').read())
    elif choice == '5':
            transition()
            exec(open('util/5_BruteForce/bruteforce.py').read())
    elif choice == '6':
            transition()
            exec(open('util/6_ThreadSpammer/ThreadSpammer.py').read())        
    elif choice == '>':
        clear()
        astraahometitle()
        print(f"""{y}[{b}+{y}]{w} Diğer seçenekler:
           
\n {y}[{w}9{y}]{w} Çıkış\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{b}<{y}]{w} Onceki Sayfa""")
        choice = input(f"""{y}[{b}#{y}]{w} Seçiminiz: """)

        if choice == '24':
            transition()
            astraahometitle()
            print(f"""                                            {y}[{b}+{y}]{w} Development Networks:\n\n                                                {y}[{w}#{y}]{w} Kurucu: ErenncanDeniz/itempazar.com/profil                                               {y}[{w}#{y}]{w} Server:    None\n\n\n                                            {y}[{b}+{y}]{w} Other Network\n\n                                                {y}[{w}#{y}]{w} Kurucu: ErenncanDeniz/itempazar.com/profil                                                  {y}[{w}#{y}]{w} Discord:   None\n\n\n\n\n""")
            input(f"""{y}[{b}#{y}]{w} Çıkmak için ENTERa basın""")
            main()
        elif choice == '25':
            transition()
            sys.exit()
        elif choice == '<':
            clear()
            main()    
        else:
            clear()
            main()
    else:
        clear()
        main()


if __name__ == "__main__":
    import sys
    setTitle("@ErencanDeniz Yükleniyor...")
    System.Size(120, 30)
    Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, time=1)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/AstraaDev/complement/raw/main/chromedriver.exe" """)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Üzgünüm ama python versionu ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
        sys.exit()
    else:
        #search_for_updates()
        clear()
        main()
