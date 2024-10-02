# -*- coding : utf-8 -*-
"""
__author__ = "Suji Namgung"
__version__ = "1.0"
"""

from retailer import Retailer
import random
from car import Car
from order import Order


class CarRetailer(Retailer):
	# Initializes instance variables
	# Retailer id and retailer name is from retailer class (parent class)
	def __init__(self,
				 retailer_id = 0,
				 retailer_name = "",
				 carretailer_address = "",
				 carretailer_business_hours = (),
				 carretailer_stock = []):
		super().__init__(retailer_id, retailer_name)
		self.carretailer_address = carretailer_address
		self.carretailer_business_hours = carretailer_business_hours
		self.carretailer_stock = carretailer_stock

	# Reset of the class methods and properties
	def __str__(self):
		return f"{super().__str__()}, {self.carretailer_address}, {self.carretailer_business_hours}, {self.carretailer_stock}"

	# Set the way of write file with path parameter for flexibility (not hardcoding)
	def write_file(self, path, data, mode):
		try:
			with open(path, mode) as f:
				f.write(data)
				return True
		except FileNotFoundError:
			print("File not found. Please check the path")
			return False

	# Open the file for reading
	# Create an empty list to store data read from a file and read a line from the file
	# Check if the line is empty, indicating the end of the file
	# And then, append the line as a string to the data list
	def load_current_stock(self, path):
		try:
			with open(path, 'r') as f:
				data = []
				while True:
					line = f.readline()
					if not line: break
					data.append(f"{line}")
				# Change all comma, space, "]" between datas to one same distinguished value  with "!"
				# And split it to change to ","
				for info in data:
					div_data = info.split(" [")
					retailer = div_data[0].split(", ")
					car_data = div_data[1].replace("\n", "").replace("]", "").replace("', '", "!").replace("'","").split("!")
					car_data = [car_info.split(", ") for car_info in car_data]
					if retailer[0] == str(self.retailer_id):
						for car_info in car_data:
							if car_info[0] not in self.carretailer_stock:
								self.carretailer_stock.append(car_info[0])
				return data
		except FileNotFoundError:
			print("File not found. Please check the path")

	# For checking current hour is business hours base on cur_hour
	def is_operating(self, cur_hour):
		if self.carretailer_business_hours[1] >= cur_hour and self.carretailer_business_hours[0] <= cur_hour:
			return True
		return False

	# For getting all stock data as a list from path of stock files
	def get_all_stock(self):
		stock_list = []
		data = self.load_current_stock("./data/stock.txt")
		for car_code in self.carretailer_stock:
			# Change all comma, space, "]" between datas to one same distinguished value  with "!"
			# And split it to change to ","
			for car_data in data:
				div_data = car_data.split(" [")
				car_data = div_data[1].replace("\n", "").replace("]", "").replace("', '", "!").replace("'", "").split("!")
				car_data = [car_info.split(", ") for car_info in car_data]
				for car_info in car_data:
					if car_info[0] == car_code:
						car = Car()
						car.car_code = car_info[0]
						car.car_name = car_info[1]
						car.car_capacity = int(car_info[2])
						car.car_horsepower = int(car_info[3])
						car.car_weight = int(car_info[4])
						car.car_type = car_info[5]
						stock_list.append(car)
		return stock_list

	# For getting postcode from stock, split carretailer address with ','
	def get_postcode_distance(self, postcode):
		extrcar_act = self.carretailer_address.split(",")[-1]
		current_postcode = extrcar_act[-4:]
		return abs(int(current_postcode) - int(postcode))

	# Remove the stock from the stock file list
	def remove_from_stock(self, car_code):
		all_data = self.load_current_stock("./data/stock.txt")
		try:
			self.carretailer_stock.remove(car_code)
		except:
			pass
		car_code_check = 0
		for car_data in all_data[:]:
			if car_data[:8] == str(self.retailer_id):
				div_data = car_data.split(" [")
				old_car_data = div_data[1].replace("\n", "").replace("]", "").replace("', '", "!").replace("'",
																										   "").split(
					"!")
				old_car_data = [car_info.split(", ") for car_info in old_car_data]
				for car_info in old_car_data[:]:
					if car_info[0] != car_code:
						new_car_info = ", ".join(car_info)
						old_car_data.append(new_car_info)
					else:
						car_code_check += 1
					old_car_data.remove(car_info)
				all_data.remove(car_data)
				all_data.append(f"{div_data[0]} {old_car_data}\n")
		if car_code_check == 0:
			return False
		return self.write_file("./data/stock.txt", "".join(all_data), "w")

	# Add the stock to the stock file list
	def add_to_stock(self, car):
		all_data = self.load_current_stock("./data/stock.txt")
		for car_data in all_data[:]:
			if car_data[:8] == str(self.retailer_id):
				div_data = car_data.split(" [")
				old_car_data = div_data[1].replace("\n", "").replace("]", "").replace("', '", "!").replace("'",
																										   "").split(
					"!")
				for car_info in old_car_data:
					if car_info[:8] == car.car_code:
						return False
				old_car_data.append(
					f"{car.car_code}, {car.car_name}, {car.car_capacity}, {car.car_horsepower}, {car.car_weight}, {car.car_type}")
				all_data.remove(car_data)
				all_data.append(f"{div_data[0]} {old_car_data}\n")
				return self.write_file("./data/stock.txt", "".join(all_data), 'w')

	# Get all stock base on car type as a list
	def get_stock_by_car_type(self, car_types):
		stock_list = []
		data = self.get_all_stock()
		for all_data in data:
			if all_data.car_type == car_types:
				stock_list.append(all_data)
		return stock_list

	# Get all stock base on car licence type as a list
	def get_stock_by_licence_type(self, licence_type):
		data = self.get_all_stock()
		if licence_type == "P" or licence_type == "p":
			stock_list = []
			for car in data:
				if car.probationary_licence_prohibited_vehicle():
					stock_list.append(car)
			return stock_list
		return data

	# Choose the car randomly from stock for recommendation
	def car_recommendation(self):
		selected_car = random.choice(self.get_all_stock())
		return selected_car

	# Get all available car stock data
	# And Find the car with the specified car_code and add it to the order list
	# Return the order object representing the selected car
	def create_order(self, car_code):
		data = self.get_all_stock()
		order_car = []
		for car in data:
			if car.car_code == car_code:
				order_car.append(car)
				break
		retailer = Retailer()
		retailer.retailer_id = self.retailer_id
		retailer.retailer_name = self.retailer_name
		import time
		order = Order(order_car=order_car[0],
					  order_retailer=retailer,
					  order_creation_time=int(time.time()))
		order.order_id = order.generate_order_id(car_code=car_code)
		order_txt = f"\n{order.order_id}, {order.order_car.car_code}, {order.order_retailer.retailer_id}, {order.order_creation_time}"
		self.remove_from_stock(car_code=car_code)
		self.write_file("./data/order.txt", order_txt, 'a')
		return order