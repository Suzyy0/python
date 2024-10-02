# -*- coding : utf-8 -*-
"""
__author__ = "Suji Namgung"
__version__ = "1.0"
"""
import random
import string

class Order:
	# Initializes instance variables
	def __init__(self, order_id = 0, order_car = "",
				 order_retailer = "", order_creation_time = ""):
		self.str_1 = "~!@#$%^&*"
		self.order_id = order_id
		self.order_car = order_car
		self.order_retailer = order_retailer
		self.order_creation_time = order_creation_time

	# Reset of the class methods and properties
	def __str__(self):
		return (f"{self.order_id}, {self.order_car}, "
				f"{self.order_retailer}, {self.order_creation_time}")

	# To get unique order id, generate string randomly and change even numbers to uppercase letter
	# And from the rest of character, calculate ascii code to the power of 2 for each character and get remainder of it
	# Use zip() to used to combine multiple iterables element-wise into tuples
	# And using enumerate for combining index and alphabet
	def generate_order_id(self, car_code):
		order_id = f"{''.join(random.sample(string.ascii_lowercase, 6))}"
		order_id = "".join([o+e.upper() for o, e in zip(order_id[::2], order_id[1::2])])
		for idx, alphabet in enumerate(order_id):
			order_id += self.str_1[(ord(alphabet) ** 2) % len(self.str_1)] * idx
		return order_id + car_code + str(self.order_creation_time)