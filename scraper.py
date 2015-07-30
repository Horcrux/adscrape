#!/usr/local/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import sys

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
    #Grab and validate telephone number
    telephonesoup=soup.findAll('a',{'class':'button telephone'})
    if telephonesoup!=[]:
        adinfo.append(telephonesoup[0]['href'])
    else:
        adinfo.append("none")
    #Grab detail
    adinfo.append(soup.findAll('span',{'class':'pre'})[0].text)
    return adinfo

adsinfo = []
for ad in getadlist(sys.argv[1]):
    adsinfo.append(scrapead(ad))
#Stuff results in a file
outfile = open(str(sys.argv[2]), 'w')
for ad in adsinfo:
    for item in ad:
        content = (item).encode('utf-8')
        outfile.write(content+"\n")
outfile.close()
