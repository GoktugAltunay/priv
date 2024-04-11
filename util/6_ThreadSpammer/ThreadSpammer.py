try:
    import requests, time, os
except:
    os.system("pip install requests")
    import requests
    import time
    import os

token = str(input(" ~ Tokeni girin: "))
channel_id = str(input(" ~ Kanal IDsini girin: "))
thread_name = str(input(" ~ Thread adini girin: "))
header = {"content-type": "application/json",
            "Authorization": token}
while True:    
    r = requests.post(f"https://canary.discord.com/api/v9/channels/{channel_id}/threads", headers=header, json={
                    "name": thread_name, "type": 11, "auto_archive_duration": 60})
    if r.status_code == 200 or r.status_code == 201:
        print(f" > Thread olusturuldu -> ID: {r.json()['id']}")
    elif r.status_code == 429:
        print(f" ! Ratelimit Yedi - Bekleniyor {r.json()['retry_after']}s")
        time.sleep(int(r.json()['retry_after']))
    else:
        print("ID Yanlis. / Ses kanalina threads acilamaz.")
