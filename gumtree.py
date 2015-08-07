#!/usr/local/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
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
    try:
        time=soup.find('meta',{'itemprop':'datePosted'})
        adinfo.append(time['content'])
    except:
        time=soup.findAll('span',{'class':'value'})
        adinfo.append (time[0].getText().strip())
    #Grab and validate telephone number
    telephonesoup=soup.findAll('a',{'class':'button telephone'})
    if telephonesoup!=[]:
        adinfo.append(telephonesoup[0]['href'])
    else:
        adinfo.append("none")
    #Grab detail
    adinfo.append(soup.findAll('span',{'class':'pre'})[0].text)
    return adinfo

def outtofile(outdata, outfile):
    with open("csvs/"+outfile, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|', quotechar='\\', quoting=csv.QUOTE_ALL)
        for ad in outdata:
            line = []
            for item in ad:
                line.append(item.encode('utf-8').replace('\r',' ').replace('\n',' '))
            writer.writerow(line)

def main(url, outfile, pages):
    adsinfo = []
    for page in range(1, pages+1):
        try:
            #for regional pages
            pageurl="http://www.gumtree.co.za/"+url.split('/')[3]+'/'+url.split('/')[4]+'/'+'page-'+str(page)+'/'+url.split('/')[5].split('p')[0]+'p'+str(page)
        except:
            #for whole of SA pages
            pageurl = "http://www.gumtree.co.za/"+url.split('/')[3]+'/'+'page-'+str(page)+'/'+url.split('/')[4].split('p')[0]+'p'+str(page) 
        for ad in getadlist(pageurl):
            adsinfo.append(scrapead(ad))
    #put results in a file
    outtofile(adsinfo, outfile.split('\n')[0])
