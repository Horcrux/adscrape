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

#Return a list of lists of ads' contents
def scrapead(url):
    r  = requests.get(url);
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    mydivs = soup.findAll("span", { "class" : "pre" })
    print (type (mydivs))
    print (mydivs)

for ad in getadlist(sys.argv[1]):
    print("ad="+ad)
    scrapead(ad)
    print("************************************************")
