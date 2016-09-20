import math, brewerydb
from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
This handles opening 
"""

page = urlopen('http://www.efficientdrinker.com/beer/complete-calories-abv.html')
soup = BeautifulSoup(page, 'html.parser')

data = []
table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) #for empty values

class Beer:
    """Beer object TODO: should account for empty OG in recommendation"""
    def __init__(self, name, abv=0, ibu=0, og=0):
        self.name = name
        self.abv = abv
        self.ibu = ibu
        self.og = og
    def similar_to(self, other):
        return math.sqrt(abs(other.abv - self.abv) + (abs(other.ibu - self.ibu))
            + abs(other.og - self.og))


l = Beer("Lagunitas Little Sumpin' Sumpin'", 7.5, 65, 1.071)
i = Beer("Lagunitas IPA", 6.2, 51.5, 1.06)
p = Beer("Lagunitas Pale Ale", 6, 35, 1.05)
s = Beer("Lagunitas Brown Shugga' Substitute Ale", 8, 63.21, 1.07)