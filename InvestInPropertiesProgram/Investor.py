from DataVisualiser import DataVisualiser
from SimpleDataAnalyser import SimpleDataAnalyser

class Investor:  # to display a menu, ask for and process user inputs, etc.
    def __init__(self):
        # Create instances of SimpleDataAnalyser and DataVisualiser classes.
        self.sda = SimpleDataAnalyser()
        self.dv = DataVisualiser()

        # Load property data from 'property_information.csv' and store it in 'df'.
        self.df = self.sda.extract_property_info('property_information.csv')

        # Extract the unique suburb names from the data and store them in 'suburb_list'.
        self.suburb_list = self.df['suburb'].unique()

        # Define a dictionary for currency exchange rates.
        self.currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY":
            4.72, "JPY": 93.87, "HKD": 5.12, "KRW": 860.92, "GBP": 0.51,
                              "EUR": 0.60, "SGD": 0.88}

        # Create a list of available currencies based on the dictionary keys.
        self.currency_list = list(self.currency_dict.keys())

    def get_command(self):
        # Method to display the menu options and get the user's command choice.
        print('\n********Main MENU********')
        print('1) Get Suburb Infomation')
        print('2) See Property Sales Trend')
        print('3) Find a Property')
        print('4) Quit Program')
        print('*************************\n')

        # Prompt the user to enter a command and return the input.
        return input('Enter command: ')

    def run(self):
        # Main execution method for the program.
        while True:
            # Enter a loop to continuously interact with the user until the program is quit.
            # Get the user's choice of action from the menu.
            # If the user chooses option 1: Get Suburb Information.
            # Display the list of available suburb names.
            option = self.get_command()
            if option == '1':
                print(self.suburb_list)
                while True:
                    # Prompt the user to enter a suburb name, with 'all' as the default option.
                    suburb = input("\nEnter the specific suburb name (but If you want all suburb's properties, enter 'all'): ")
                    if suburb not in self.suburb_list and suburb != 'all':
                        print('No such suburb found.')
                    else:
                        break

                # Call methods to summarize suburb data and average land size.
                self.sda.suburb_summary(self.df, suburb)
                self.sda.avg_land_size(self.df, suburb)

                # Display the list of available currencies and prompt the user to choose one.
                print(self.currency_list)
                currency = input('Enter currency: ')

                if currency.upper() not in self.currency_list:
                    # Check if the entered currency is valid; if not, use 'AUD' as the default.
                    print("No such currency found, use 'AUD' as default.")
                    currency = 'AUD'
                # Visualize property value distribution for the selected suburb and currency.
                self.dv.prop_val_distribution(self.df, suburb, currency.upper())
            elif option == '2':
                # If the user chooses option 2: Call the method to visualize the sales trend of properties.
                self.dv.sales_trend(self.df)
            elif option == '3':
                # If the user chooses option 3: Display the list of available suburb names.
                print(self.suburb_list)
                while True:
                    # While loop to ensure the selected suburb is valid.
                    # Check if the entered suburb is valid; if not, inform the user.
                    suburb = input('Enter suburb name: ')
                    if suburb not in self.suburb_list:
                        print('No such suburb found.')
                    else:
                        break

                while True:
                    # While loop to ensure the entered price is a valid integer.
                    # Check if the entered suburb is integer; if not, inform the user.
                    price = input('Enter price: ')
                    if not price.isdigit():
                        print('Invalid input.')
                    else:
                        break

                if self.sda.locate_price(price, self.df, suburb):
                    # Call the method to locate the specified price in the selected suburb.
                    print('\nFound price with', price, 'in', suburb + '.')
                    print("\n")
                else:
                    print('Cannot find price with', price, 'in', suburb + '.')
                    print("\n")

            elif option == '4':
                # If the user chooses option 4: Quit the program, exit the loop.
                break
            else:
                # Inform the user if an invalid command is entered.
                print('Wrong command!')
