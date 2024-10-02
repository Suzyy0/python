# -*- coding : utf-8 -*-
"""
__author__ = "Suji Namgung"
__version__ = "1.0"
"""

import random
import string


class Car:
    # Initializes instance variables
    def __init__(self,
                 car_code="",
                 car_name="",
                 car_capacity=0,
                 car_horsepower=0,
                 car_weight=0,
                 car_type=""):
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    # Reset of the class methods and properties
    def __str__(self):
        return f"{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, {self.car_type}"

    # Make condition of licence prohibited vehicle
    def probationary_licence_prohibited_vehicle(self):
        power_mass_ratio = (self.car_horsepower / (self.car_weight / 1000)) * 1000
        return power_mass_ratio > 130

    # Matching the car founded
    def found_matching_car(self, car_code):
        return self.car_code == car_code

    # Getting car type
    def get_car_type(self):
        return self.car_type

    # Getting car code randomly
    def generate_car_code(self, list_car):
        while True:
            car_code = f"{''.join(random.sample(string.ascii_uppercase, 2))}{''.join(random.choice(string.digits) for i in range(6))}"
            if car_code not in list_car:
                self.car_code = car_code
                break