import brewerydb
from scraper import Beer

API_KEY = '85a0b8dd9751bdb98e0d8ccea06b7e54'
BASE_URI = 'http://api.brewerydb.com/v2/?key='

bd = brewerydb.BreweryDb
bd.configure(API_KEY)

hoppies = bd.beers({'ibu':+50})['data']


def clean_and_parse(data):
    # data should be in 
    b = []
    for beer in data:
        try:
            name = beer['name']
            abv = beer['abv']
            ibu = beer['ibu']
            og = beer['originalGravity']
        except Exception as e:
            og = 0
        b.append(Beer(name, abv, ibu, og))
    return b

