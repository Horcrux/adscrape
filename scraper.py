#!/usr/local/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import sys
import csv

#Return a list of URLs of ads
def getadlist(url):
    r  = requests.get(url);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    ads = []
    for link in soup.find_all('a'):
        if (link.get('href').startswith("/a-")):
            ads.append("http://www.gumtree.co.za"+link.get('href'))
    return ads

#Return a list of ads' contents
def scrapead(url):
    r  = requests.get(url);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    adinfo = []
    #Grab title
    titlesoup=soup.findAll('span',{'class':'myAdTitle'})
    adinfo.append(titlesoup[0].string)
    #Grab time of post
    time=soup.find('meta',{'itemprop':'datePosted'})
    adinfo.append(time['content'])
    #Grab and validate telephone number
    telephonesoup=soup.findAll('a',{'class':'button telephone'})
    if telephonesoup!=[]:
        adinfo.append(telephonesoup[0]['href'])
    else:
        adinfo.append("none")
    #Grab detail
    adinfo.append(soup.findAll('span',{'class':'pre'})[0].text)
    return adinfo

def outtofile(outdata):
    with open(sys.argv[2], 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|', quotechar='\\', quoting=csv.QUOTE_ALL)
        for ad in adsinfo:
            line = []
            for item in ad:
                line.append(item.encode('utf-8').replace('\r',' ').replace('\n',' '))
            writer.writerow(line)
    exit()

def outtoterminal(outdata):
    for ad in adsinfo:
        for item in ad:
            content = (item).encode('utf-8').replace('\r',' ').replace('\n',' ')
            print(content+"\n")
    
adsinfo = []
for ad in getadlist(sys.argv[1]):
    adsinfo.append(scrapead(ad))
#put results in a file or dump to terminal
try:
    outtofile(adsinfo)
except:
    outtoterminal(adsinfo)
