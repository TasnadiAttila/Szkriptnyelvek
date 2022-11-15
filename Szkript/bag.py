

from operator import le
from re import T


class Bag:
    def __init__(self):
        self.adatok = []    

    def add (self,v):
        self.adatok.append(v)
    def add_twice(self,v):
        self.adatok.append(v)
        self.adatok.append(v)

    def __str__(self):
        return str(self.adatok)[1:-1]

    def __len__(self):
        return len(self.adatok)
    
    def __lt__(self,other):
        return len(self) < len(other)
    def __eq__(self,other):
        return len(self) == len(other)
    def __gt__(self,other):
        return len(self) > len(other)
    

def main():
    bag = Bag()
    empty_bag = Bag()

    bag.add(12)
    bag.add_twice(13)

    a = str(bag)

    if empty_bag < bag:
        print("Kevesebb elem")
    if empty_bag.__gt__(bag) == False:
        print("Több elem")
    if bag.__gt__(empty_bag) == True:
        print("gyanannyi")


if __name__ == "__main__":
    main()