import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from multiprocessing import Process, Queue, Pool
import threading
import sys
from time import sleep


def get_data(i,url):    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content)
    tags = soup.findAll('span', attrs={'class':'list-identifier'})

    for tag in tags:
        i += 1
        img_tag = tag.find('a', attrs={'title': 'Download PDF'})
        save_papers("https://arxiv.org" + img_tag['href'], str(i) + ".pdf")

    # sleep(5)
    return i


def save_papers(image_url, filename):
    response = requests.get(image_url, stream=True)
    if not response.ok:
        print(response)
        return

    img_data = response.content
    filename = "./papers/"+filename
    with open(filename, 'wb') as handler:
        handler.write(img_data)

    print(filename)



i=1

get_data(i,"https://arxiv.org/list/cs/new")
