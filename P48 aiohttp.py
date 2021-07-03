import aiohttp
import asyncio
import time

start=time.time()
#ip地址为远程服务器
urls=[
"http://121.5.154.239:10086/tom",
    "http://121.5.154.239:10086/bobo",
    "http://121.5.154.239:10086/jay"
]
async def fetch(client,url):
    async with client.get(url) as resp:
        assert resp.status == 200
        ret= await resp.text()
        print(ret)

async def main():
    tasks = []
    print("main start")
    async with aiohttp.ClientSession() as client:
        for url in urls:
            tasks.append(asyncio.create_task(fetch(client,url), name=url.split("/")[-1]))
        done, pending = await asyncio.wait(tasks)
        print(done)





asyncio.run(main())
end=time.time()
print("time",end-start)