from bs4 import BeautifulSoup
import requests

adlist="http://www.gumtree.co.za/s-dj-entertainment-services/bellville/v1c9269l3100037p1"

def getadlist(url):
    r  = requests.get(url);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    ads = []
    #Links to listings
    for link in soup.find_all('a'):
        if (link.get('href').startswith("/a-")):
            ads.append("http://www.gumtree.co.za"+link.get('href'))
    return ads

def scrapead(url):
    r  = requests.get(url);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    mydivs = soup.findAll("span", { "class" : "pre" })
    print (type (mydivs))
    print (mydivs)

for ad in getadlist(adlist):
    scrapead(ad)
    print("************************************************")
