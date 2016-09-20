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
    """Beer object"""
    def __init__(self, abv, ibu, og):
        self.abv = abv
        self.ibu = ibu
        self.og = og
    def similar_to(self, other):
        pass
