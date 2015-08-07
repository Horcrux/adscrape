#!/usr/local/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import csv
user_agent = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

#Return a list of URLs of ads
def getadlist(url):
    r  = requests.get(url, headers = user_agent);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    ads = []
    for link in soup.find_all('a',{'data-qa':'list-item'}):
        ads.append(link['href'])
    return ads

#Return a list of ads' contents
def scrapead(url):
    r  = requests.get(url, headers = user_agent);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    adinfo = []
    #Grab title
    titlesoup=soup.findAll('h2',{'class':'item-title'})
    adinfo.append(titlesoup[0].string)
    #Grab time of post
    try:
        time=soup.find('time')
        adinfo.append(time.string)
    except:
        time=soup.findAll('span',{'class':'value'})
        adinfo.append (time[0].getText().strip())
    #Grab and validate telephone number
    telephonesoup=soup.findAll('p',{'class':'icons icon-phone user-phone'})
    if telephonesoup!=[]:
        adinfo.append(telephonesoup[0].getText())
    else:
        adinfo.append("none")
    #Grab detail
    adinfo.append(soup.findAll('div',{'class':'text'})[0].text.strip())
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
        pageurl = url + '-p-' + str(page)
        for ad in getadlist(pageurl):
            adsinfo.append(scrapead(ad))
    #put results in a file
    outtofile(adsinfo, outfile.split('\n')[0])
