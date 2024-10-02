# -*- coding : utf-8 -*-
"""
__author__ = "Suji Namgung"
__version__ = "1.0"
"""

import random
import string
from retailer import Retailer
from car_retailer import CarRetailer
from car import Car

# Create the main menu
def main_menu():
	print("\n")
	print("=" * 20 + "Main MENU" + "=" * 20)
	print("a) Look for the nearest car retailer")
	print("b) Get car purchase advice")
	print("c) Place a car order")
	print("d) Exit")
	print("=" * 50)
	print("\n")

# Create the sub menu for showing it when users select option 'b' of the main menu
def sub_menu():
	print("=" * 15 + " Advice options " + "=" * 15)
	print("1) Recommended a car")
	print("2) Get all cars in stock")
	print("3) Get cars in stock by car types")
	print("4) Get probationary licence permitted cars in stock")
	print("5) Back to main menu")
	print("=" * 50)

# Initialize an empty list to store values
# Then It will store the values randomly according the each of conditions and ranges
# And it will be using in main methods
def generate_test_data(cnt):
	retailer_id_list = []
	car_code_list = []
	data = []
	# The loop is executed cnt times, but the loop variable _ is not used within the loop body.
	# Because I only care the number of iterations, not variable itself
	for _ in range(0, cnt):
		retailer = Retailer(retailer_name="".join(random.sample(string.ascii_letters + " ", 10)))
		retailer.generate_retailer_id(retailer_id_list)

		address_list = [
			"Clayton Rd Clayton",
			"Clayton Rd Mount Waverley",
			"N D GRANGEVILLE ID",
			"W MONTE VISTA PHOENIX AZ"
		]
		retailer_address = random.choice(address_list)
		post_code = random.randint(1000, 9999)
		total_retailer_address = f"{retailer_address}, VIC{post_code}"

		# Set the business hours as a tuple of floats
		# using uniform(a,b) for getting random floating-point number between a and b
		business_hour_start = float(f"{random.uniform(0, 11) : 0.1f}".replace(" ", ""))
		business_hour_end = float(f"{random.uniform(12, 24) : 0.1f}".replace(" ", ""))
		business_hour = (business_hour_start, business_hour_end)
		car_retailer = CarRetailer(retailer_id=retailer.retailer_id,
								   retailer_name=retailer.retailer_name,
								   carretailer_address=total_retailer_address,
								   carretailer_business_hours=business_hour)
		# Create four cars information randomly
		car_list = []
		for _ in range(0, 4):
			car = Car()
			car.generate_car_code(car_code_list)
			car.car_name = "".join(random.sample(string.ascii_letters + " ", random.randint(15, 20)))
			car.car_capacity = random.randint(1, 20)
			car.car_horsepower = random.randint(100, 150)
			car.car_weight = random.randint(1000, 2000)
			car_type_list = ["FWD", "RWD", "AWD"]
			car.car_type = random.choice(car_type_list)
			car_list.append(car)

		# Add retailer, car_retailer, car_list information to data
		data.append({'retailer': retailer,
					 'car_retailer': car_retailer,
					 'car_list': car_list})
	return data

# Attempt to open the file for writing
# Extract car retailer information from data and convert it to a string
# Add the car list to the write string
def generate_test_data_file(path, test_data):
	try:
		with open(path, 'w') as file:
			for data in test_data:
				write_str = f"{','.join(data['car_retailer'].__str__().split(',')[:-1])}"
				car_list = []
				for car_data in data['car_list']:
					car_list.append(
						f"{car_data.car_code}, {car_data.car_name}, {car_data.car_capacity}, {car_data.car_horsepower}, {car_data.car_weight}, {car_data.car_type}")
				write_str += f", {car_list}\n"
				file.write(write_str)
	except FileNotFoundError:
		print("file not found")

# Read data from a file, parase it, and creates objects to represent retailers and cars
# Initialize a list to store data for test_data, and lines from the file for data
def update_test_data(path):
	try:
		with open(path, 'r') as f:
			test_data = []
			data = []
			while True:
				line = f.readline()
				if not line: break
				data.append(f"{line}")
			# Split the line into retailer and car data
			for info in data:
				div_data = info.split(" [")
				retailer_data = div_data[0].split(", ")
				# Create Retailer and CarRetailer objects
				retailer = Retailer(retailer_id=retailer_data[0],
									retailer_name=retailer_data[1])
				car_retailer = CarRetailer(retailer_id=retailer_data[0],
										   retailer_name=retailer_data[1],
										   carretailer_address=f"{retailer_data[2], {retailer_data[3]} }",
										   carretailer_business_hours=tuple(retailer_data[4]))
				# Change all comma, space, "]" between datas to one same distinguished value  with "!"
				# And split it to change to ","
				car_data = div_data[1].replace("\n", "").replace("]", "").replace("', '", "!").replace("'", "").split(
					"!")
				car_data = [car_info.split(", ") for car_info in car_data]
				# Initialize a list to store Car objects
				# And loop through car data and create Car objects
				car_list = []
				for car_info in car_data:
					car = Car()
					car.car_code = car_info[0]
					car.car_name = car_info[1]
					car.car_capacity = int(car_info[2])
					car.car_horsepower = int(car_info[3])
					car.car_weight = int(car_info[4])
					car.car_type = car_info[5]
					car_list.append(car)
				test_data.append({'retailer': retailer,
								  'car_retailer': car_retailer,
								  'car_list': car_list})
	except FileNotFoundError:
		print("file not found")


if __name__ == "__main__":
	# Generate test data and save it to a file
	test_data = generate_test_data(cnt=3)
	generate_test_data_file("./data/stock.txt", test_data=test_data)
	# Print a welcome message at first
	print("\nWelcome to Car Purchase Advisor Application")
	print("Are you considering to buy the car? Then, Get some advice from our retailers!")
	print("We'll find the nearest retaliers around your place for helping you.")
	print("If you're interested in, select options of the main Menu.")
	# Display the main menu for user input
	main_menu()
	while True:
		user_input = input()
		# If user input is 'a', ask user to input postcode and display the nearest retailer
		if user_input == "a" or user_input == "A":
			try:
				post_code_input = input("\nEnter your post code: ")
				min_distance = -1
				selected_car_retailer = None
				# Find the nearest car retailer according the user's postcode
				for data in test_data:
					dist = data['car_retailer'].get_postcode_distance(post_code_input)
					if (min_distance != -1 and min_distance > dist) or min_distance == -1:
						min_distance = dist
						selected_car_retailer = data
				# Print information of retailer ID and Name about the nearest retailer
				print("\nHere is the nearest car retailer.")
				print("*" * 15 + " Retailer Info " + "*" * 20)
				print(f"Retailer ID : {selected_car_retailer['retailer'].retailer_id}")
				print(f"Retailer Name : {selected_car_retailer['retailer'].retailer_name}")
				print("*" * 50 + "\n")
				print("Need more advice from retailers? Then, Select 'b' of Main Menu.")
				print("Firstly You'll get the list of retailers.")
				main_menu()
			# Display it for the invalid input
			except:
				print("Wrong postcode. Please restart. Select Main Menu again.")
				main_menu()
		# If user input is 'b', display the list of randomly chose retailers
		elif user_input == "b" or user_input == "B":
			print("\n\n\nThis is the list of retailers.")
			print("\n" + "*" * 15 + " Retailers List " + "*" * 20)
			for idx, data in enumerate(test_data):
				print(f"Retailer ID : {data['retailer'].retailer_id}")
				print(f"Retailer Name : {data['retailer'].retailer_name}\n")
			print("*" * 50 + "\n")
			selected_retailer_id = input("For selecting only one retailer, Enter the retailer ID: ")
			print("\n\nThe retailer will give you advice according to options.\n")
			sub_menu()
			sub_user_input = input("\nCheck and select one option : ")

			# Display the recommendation base on car info
			# If user input is 1, display one recommendation
			if sub_user_input == "1":
				for data in test_data:
					if data['retailer'].retailer_id == selected_retailer_id:
						print("\nThis is the recommendation about the car.")
						print("-" * 50)
						print(f"Car ID : {data['car_retailer'].car_recommendation().car_code}")
						print(f"Car Name : {data['car_retailer'].car_recommendation().car_name}")
						print(f"Car Capacity : {data['car_retailer'].car_recommendation().car_capacity}")
						print(f"Car Horsepower : {data['car_retailer'].car_recommendation().car_horsepower}")
						print(f"Car Weight : {data['car_retailer'].car_recommendation().car_weight}")
						print(f"Car Type : {data['car_retailer'].car_recommendation().car_type}")
						print("-" * 50)
						print("\nHow's the advice? If you finished to check, go to Main MENU to order or exit.")
						main_menu()
						break
			# If user input is 2, display the list of recommendation
			elif sub_user_input == "2":
				for data in test_data:
					if data['retailer'].retailer_id == selected_retailer_id:
						print("\nThis is the recommendation about the car.")
						all_stock = data['car_retailer'].get_all_stock()
						print("=" * 50)
						for car in all_stock:
							print("-" * 50)
							print(f"Car ID : {car.car_code}")
							print(f"Car Name : {car.car_name}")
							print(f"Car Capacity : {car.car_capacity}")
							print(f"Car Horsepower : {car.car_horsepower}")
							print(f"Car Weight : {car.car_weight}")
							print(f"Car Type : {car.car_type}")
						print("=" * 50)
						print("\nHow's the advice? If you finished to check, go to Main MENU to order or exit.")
						main_menu()
						break
			# If user input is 3, display the list of recommendation base on type of cars
			elif sub_user_input == "3":
				for data in test_data:
					if data['retailer'].retailer_id == selected_retailer_id:
						car_type = input("Enter car type: ")
						print("\nThis is the recommendation about the car.")
						all_stock_by_car_type = data['car_retailer'].get_stock_by_car_type(car_type)
						print("=" * 50)
						for car in all_stock_by_car_type:
							print("-" * 50)
							print(f"Car ID : {car.car_code}")
							print(f"Car Name : {car.car_name}")
							print(f"Car Capacity : {car.car_capacity}")
							print(f"Car Horsepower : {car.car_horsepower}")
							print(f"Car Weight : {car.car_weight}")
							print(f"Car Type : {car.car_type}")
						print("=" * 50)
						print("\nHow's the advice? If you finished to check, go to Main MENU to order or exit.")
						main_menu()
						break
			# If user input is 4, display the list of recommendation base on permitted cars
			elif sub_user_input == "4":
				for data in test_data:
					if data['retailer'].retailer_id == selected_retailer_id:
						print("\nThis is the recommendation about the car.")
						all_stock__probationary_licence_permitted_cars = data['car_retailer'].get_stock_by_licence_type(
							"P")
						print("=" * 50)
						for car in all_stock__probationary_licence_permitted_cars:
							print("-" * 50)
							print(f"Car ID : {car.car_code}")
							print(f"Car Name : {car.car_name}")
							print(f"Car Capacity : {car.car_capacity}")
							print(f"Car Horsepower : {car.car_horsepower}")
							print(f"Car Weight : {car.car_weight}")
							print(f"Car Type : {car.car_type}")
						print("=" * 50)
						print("\nHow's the advice? If you finished to check, go to Main MENU to order or exit.")
						main_menu()
						break
			elif sub_user_input == "5":
				main_menu()
			else:
				print("Wrong option. Enter the correct option.")
		# If user input is 'c', ask to input retailer ID and car ID for updating on stock.txt file
		elif user_input == "c" or user_input == "C":
			try:
				ids = input("\nEnter the retailer ID & car ID separated by spaces: ")
				retailer_id = ids.split(" ")[0]
				car_code = ids.split(" ")[1]
				cnt = 0
				# Iterate through the test data to find a matching retailer ID
				for data in test_data:
					# Check if the retailer is available according to business hour from the current time
					# Create an order and display car info
					if data['retailer'].retailer_id == retailer_id:
						import time
						if data['car_retailer'].is_operating(time.localtime().tm_hour):
							order = data['car_retailer'].create_order(car_code)
							print("Thanks for order! Your order details is below :")
							print(order.__str__())
							cnt += 1
							# Update the test data to the stock file
							update_test_data("./data/stock.txt")
							print("Back to Main MENU to exit.")
							main_menu()
						break
				# If it is not business hours, display invalids message
				if cnt == 0:
					print("Sorry, It is not business working hours. Try next time.")
			# Handle exceptions if users input wrong ID
			except:
				print("Wrong ID. Please restart. Select Main Menu again.")
				main_menu()
		elif user_input == "d" or user_input == "D":
			print("\nThanks for using it. Good bye.\n")
			break
		else:
			print("Wrong option. Enter the correct option.")