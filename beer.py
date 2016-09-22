"""
The Beer class lives here.
"""
import math

class Beer:
    """Beer object TODO: should account for empty OG in recommendation"""
    def __init__(self, name, abv=0, ibu=0, og=0):
        self.name = name
        self.abv = abv
        self.ibu = ibu
        self.og = og
        self.att_lst = [abv, ibu, og]

    def _elems(self):
        attributes = []
        if self.abv != 0:
            attributes.append(0)
        if self.ibu != 0:
            attributes.append(1)
        if self.og != 0:    
            attributes.append(2)
        return attributes

    def similar_to(self, other):
        sim = list(set(self._elems()) & set(other._elems()))
        if len(sim) > 0:
            return math.sqrt(sum([abs(self.att_lst[n] - other.att_lst[n]) for n in sim]))
        else:
            raise ValueError("These Beers dont share any similar characteristics.\
                How do you expect me to compare them?")
        

l = Beer("Lagunitas Little Sumpin' Sumpin'", 7.5, 65, 1.071)
i = Beer("Lagunitas IPA", 6.2, 51.5, 1.06)
p = Beer("Lagunitas Pale Ale", 6, 35, 1.05)
s = Beer("Lagunitas Brown Shugga' Substitute Ale", 8, 63.21, 1.07)
f = Beer("Lorem ipsum...", 9, 100, 0)