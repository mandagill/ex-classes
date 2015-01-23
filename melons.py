"""This file should have our melon-type classes in it."""

class Watermelon(object):
    def __init__(self):
        name = "watermelon"
        color = "green"
        origin = "domestic" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        shape = "natural"
        seasons = ['Fall', 'Summer']

    def get_price(self,qty):
        pricetag = 5.0
        if qty >= 3:
            price = pricetag * qty * (0.75)
        else:
            price = pricetag * qty
        return price


class Cantaloupe(object):
    def __init__(self):
        name = "cantaloupe"
        color = "tan"
        origin = "domestic" #we may want to make this a boolean later for easier price calculating, will see how that goes 
        shape = "natural"
        seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        pricetag = 5.0
        if qty >= 5:
            price = pricetag * qty * (0.50)
        else:
            price = pricetag * qty
        return price


