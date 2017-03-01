#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Hollywood%2C+FL"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

# for link in links:
#     print "<a href='%s'>%s</a>" %(link.get("href"), link.text)


g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print item.contents[0].find_all("span", {"itemprop": "name"})[0].text

    try:
        print item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
    except:
        pass

    try:
        print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text \
            + item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text \
            + " " + item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
    except:
        pass

    try:
        print item.contents[1].find_all("div", {"itemprop": "telephone"})[0].text
    except:
        pass

    print ""


