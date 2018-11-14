import time
from datetime import datetime as dt

hosts_temp = "K:\Kedar\Study\Atom\Website Blocker\hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com", "www.chess.com"]

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("Why would you open that during working hours? Get back to work!")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("Relax and rejuvinate")
    time.sleep(5)
