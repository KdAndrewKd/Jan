import asyncio
import requests
from datetime import datetime
import aiohttp
from bs4 import BeautifulSoup
from fun_randomHeaders import *
from random import choice

urls = []
responsList1 = []

with open("ИванвListUrls_9.txt", "r", encoding="utf-8")as f_content:
    listUrls = f_content.readlines()
    urls = []
    for line in listUrls:
        line = line.replace(" \n" , "")
        urls.append(line)


# Вариант асинхронного кода
async def fun_async_http(url):
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
    # async with aiohttp.ClientSession() as session:
        async with session.get(url, ) as resp:
            # print(resp.status)
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')
            soup.prettify()
            print(soup.title)


async def main(urls):

    

    tStart = datetime.now()
    await asyncio.gather(*(fun_async_http(url) for url in urls))
    # print(responsList2)
    print("\nВремя выполнения:",datetime.now() - tStart)
    



    





if __name__ == '__main__':
    asyncio.run(main(urls))
    

