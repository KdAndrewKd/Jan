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


# Вариант блокируещего кода
async def fun_blocking(url):

    desktop_agents = [

    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
                 
    ]

    def random_headers():
        return {'User-Agent': choice(desktop_agents)}

    resp = requests.get(url, headers=random_headers()).text
    # responsList1.append(resp.status_code)

    soup = BeautifulSoup(resp, 'html.parser')
    soup.prettify()
    print(soup.title)




async def main(urls):

    tStart = datetime.now()
    await asyncio.gather(*(fun_blocking(url) for url in urls))
    




    print(responsList1)
    print("\nВремя выполнения:",datetime.now() - tStart, "\n\n")

    





if __name__ == '__main__':
    asyncio.run(main(urls))
    

