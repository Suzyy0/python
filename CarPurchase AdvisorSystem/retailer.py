# -*- coding : utf-8 -*-
"""
__author__ = "Suji Namgung"
__version__ = "1.0"
"""

import random

# Parent class of car_retailer class
class Retailer:
    # Initializes instance variables
    def __init__(self, retailer_id=0, retailer_name=""):
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    # Reset of the class methods and properties
    def __str__(self):
        return f"{self.retailer_id}, {self.retailer_name}"

    # To create retailer ID randomly, set the certain range
    def generate_retailer_id(self, list_retailer):
        while True:
            new_retailer_id = str(random.randint(10000000, 99999999))
            if new_retailer_id not in list_retailer:
                self.retailer_id = new_retailer_id
                break