from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

website = r"https://en.wikipedia.org/wiki/search?q="

responseObj = urllib.request.urlopen(website)

def getSites(site):
    arr = site.split()
    site_formatted = "+".join(map(str, arr))
    website = r"https://www.lightdl.xyz/search?q={query}".format(query = site_formatted)
    
    responseObj = urllib.request.urlopen(website)

    soup = BeautifulSoup(responseObj,'html.parser')

    link_divs = soup.find_all("div",{"class":"post"})
    
    links = []

    for div in link_divs:
        a_tag = div.find("a", href = True)
        href = a_tag["href"]
        links.append(href)
        print(href)

    return links 

def getLinks(url):
    website = r"{site}".format(site = url)
    responseObj = urllib.request.urlopen(website)
    soup = BeautifulSoup(responseObj,'html.parser')

    link_divs = soup.find_all("div",{"class":"post-body"})
    
    links = []
    a_tags = []
    for div in link_divs:
        a_tag_array = div.find_all("a", href = True)
        a_tags += a_tag_array
    
    for a_tag in a_tags:
        inner_text = a_tag.get_text()
        href = a_tag["href"]
        links.append(href)
        print(inner_text +"             "+ href)
        # print(a_tag)

    # return links 


sites = getSites("family guy")
getLinks(sites[0])



