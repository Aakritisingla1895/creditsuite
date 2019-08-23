import json
import os
import requests
from bs4 import BeautifulSoup as BS
from googlesearch import search
from pprint import pprint
import os

import importlib 

import sys


from get_rrd_documents import get_article_title, get_google_result


def get_proxy():
    proxy=requests.get('http://34.213.20.241/?Key=PROFEZA').text.split('\\')[1][1:]
    return proxy

def scrape_author_details(result):
    i=1
    while i>0:
        if i<=100:
            try:
                proxies = {'https': 'https://'+ get_proxy()}
                repo = requests.get(result, proxies=proxies,timeout=10)
                print('Our work is done.')
                break
            except:
                i+=1
                print("pass")
                continue
            else:
                print("under 50 count, website is blocking our proxy.")
                break
    soup = BS(repo.text, 'lxml')
    print (soup)
    #return True

scrape_author_details()
