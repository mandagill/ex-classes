"""This file should have our melon-type classes in it."""

class Melon(object):
    BASE_MELON_PRICE = 5.00


class Watermelon(Melon):
    def __init__(self):
        self.name = "watermelon"
        self.color = "green"
        self.origin = "domestic" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Fall', 'Summer']

    def get_price(self,qty):
        pricetag = self.BASE_MELON_PRICE
        if qty >= 3:
            price = pricetag * qty * (0.75)
        else:
            price = pricetag * qty
        return price


class Cantaloupe(Melon):
    def __init__(self):
        self.name = "cantaloupe"
        self.color = "tan"
        self.origin = "domestic" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        pricetag = self.BASE_MELON_PRICE
        if qty >= 5:
            price = pricetag * qty * (0.50)
        else:
            price = pricetag * qty
        return price


class Casaba(Melon):
    def __init__(self):
        self.name = "casaba"
        self.color = "green"
        self.origin = "imported" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self,qty):
        pricetag = (self.BASE_MELON_PRICE+1.0) *1.5
        return pricetag*qty

class Sharlyn(Melon):
    def __init__(self):
        self.name = "sharlyn"
        self.color = "tan"
        self.origin = "imported" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Summer']

    def get_price(self,qty):
        pricetag = self.BASE_MELON_PRICE*1.5
        return pricetag*qty


class SantaClaus(Melon):
    def __init__(self):
        self.name = "santa claus"
        self.color = "green"
        self.origin = "imported" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Winter', 'Spring']

    def get_price(self,qty):
        pricetag = self.BASE_MELON_PRICE *1.5
        return pricetag*qty


class Christmas(Melon):
    def __init__(self):
        self.name = "christmas"
        self.color = "green"
        self.origin = "domestic" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Winter']

    def get_price(self,qty):
        pricetag = self.BASE_MELON_PRICE
        return pricetag*qty


class HornedMelon(Melon):
    def __init__(self):
        self.name = "horned melon"
        self.color = "yellow"
        self.origin = "imported" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Summer']

    def get_price(self,qty):
        pricetag = self.BASE_MELON_PRICE *1.5
        return pricetag*qty


class Xigua(Melon):
    def __init__(self):
        self.name = "xigua"
        self.color = "black"
        self.origin = "imported" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "square"
        self.seasons = ['Summer']

    def get_price(self,qty):
        # This is one bougie melon. The Amex Black of melons. 
        pricetag = self.BASE_MELON_PRICE * 1.5 * 2
        return pricetag * qty


class Ogen(Melon):
    def __init__(self):
        self.name = "ogen"
        self.color = "tan"
        self.origin = "domestic" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        self.shape = "natural"
        self.seasons = ['Spring','Summer']

    def get_price(self,qty):
        # This is one bougie melon. The Amex Black of melons. 
        pricetag = self.BASE_MELON_PRICE + 1
        return pricetag * qty