import pandas as pd


class SimpleDataAnalyser:  # to deal with the loading of data as well as the simple analyses
    def extract_property_info(self, file_path):
        # Class for handling data loading and simple analyses
        try:
            return pd.read_csv(file_path) # Read a CSV file and return it as a DataFrame
        except:
            print('No such file.') # Handle exceptions if the file does not exist
            return None

    def currency_exchange(self, dataframe, exchange_rate):
        # Method to convert the 'price' column in the DataFrame to the given exchange rate
        dataframe['price'] = dataframe['price'].mul(exchange_rate)
        return dataframe

    def suburb_summary(self, dataframe, suburb='all'):
        # Method to print summary information for suburbs
        print("\n")
        print("*" * 40)
        print("This is the summary of the property.")
        print("\n")
        if suburb == 'all':
            for sub in dataframe['suburb'].unique():

                # Print information for each suburb
                # Print mean, standard deviation, median, minimum,
                # and maximum for the number of bedrooms, bathrooms and parking spaces
                print(sub + " Bedrooms Informations")
                print(sub + " Mean", dataframe.loc[dataframe['suburb'] == sub]['bedrooms'].mean())
                print(sub + " Standard Deviation", dataframe.loc[dataframe['suburb'] == sub]['bedrooms'].std())
                print(sub + " Median", dataframe.loc[dataframe['suburb'] == sub]['bedrooms'].median())
                print(sub + " Minimum", dataframe.loc[dataframe['suburb'] == sub]['bedrooms'].min())
                print(sub + " Maximum", dataframe.loc[dataframe['suburb'] == sub]['bedrooms'].max())
                print("\n")

                print(sub + " Bathrooms Informations")
                print(sub + " Mean", dataframe.loc[dataframe['suburb'] == sub]['bathrooms'].mean())
                print(sub + " Standard Deviation", dataframe.loc[dataframe['suburb'] == sub]['bathrooms'].std())
                print(sub + " Median", dataframe.loc[dataframe['suburb'] == sub]['bathrooms'].median())
                print(sub + " Minimum", dataframe.loc[dataframe['suburb'] == sub]['bathrooms'].min())
                print(sub + " Maximum", dataframe.loc[dataframe['suburb'] == sub]['bathrooms'].max())
                print("\n")

                print(sub + " Parking Lots Informations")
                print(sub + " Mean", dataframe.loc[dataframe['suburb'] == sub]['parking_spaces'].mean())
                print(sub + " Standard Deviation", dataframe.loc[dataframe['suburb'] == sub]['parking_spaces'].std())
                print(sub + " Median", dataframe.loc[dataframe['suburb'] == sub]['parking_spaces'].median())
                print(sub + " Minimum", dataframe.loc[dataframe['suburb'] == sub]['parking_spaces'].min())
                print(sub + " Maximum", dataframe.loc[dataframe['suburb'] == sub]['parking_spaces'].max())
        else:
            if suburb not in dataframe['suburb'].unique():
                print("No such suburb found.")
            else:
                # Print information for the specified suburb
                print(suburb + " Bedrooms Informations")
                print(suburb + " Mean", dataframe.loc[dataframe['suburb'] == suburb]['bedrooms'].mean())
                print(suburb + " Standard Deviation", dataframe.loc[dataframe['suburb'] == suburb]['bedrooms'].std())
                print(suburb + " Median", dataframe.loc[dataframe['suburb'] == suburb]['bedrooms'].median())
                print(suburb + " Minimum", dataframe.loc[dataframe['suburb'] == suburb]['bedrooms'].min())
                print(suburb + " Maximum", dataframe.loc[dataframe['suburb'] == suburb]['bedrooms'].max())
                print("\n")

                print(suburb + " Bathrooms Informations")
                print(suburb + " Mean", dataframe.loc[dataframe['suburb'] == suburb]['bathrooms'].mean())
                print(suburb + " Standard Deviation", dataframe.loc[dataframe['suburb'] == suburb]['bathrooms'].std())
                print(suburb + " Median", dataframe.loc[dataframe['suburb'] == suburb]['bathrooms'].median())
                print(suburb + " Minimum", dataframe.loc[dataframe['suburb'] == suburb]['bathrooms'].min())
                print(suburb + " Maximum", dataframe.loc[dataframe['suburb'] == suburb]['bathrooms'].max())
                print("\n")

                print(suburb + " Parking Lots Informations")
                print(suburb + " Mean", dataframe.loc[dataframe['suburb'] == suburb]['parking_spaces'].mean())
                print(suburb + " Standard Deviation", dataframe.loc[dataframe['suburb'] == suburb]['parking_spaces'].std())
                print(suburb + " Median", dataframe.loc[dataframe['suburb'] == suburb]['parking_spaces'].median())
                print(suburb + " Minimum", dataframe.loc[dataframe['suburb'] == suburb]['parking_spaces'].min())
                print(suburb + " Maximum", dataframe.loc[dataframe['suburb'] == suburb]['parking_spaces'].max())

    def avg_land_size(self, dataframe, suburb='all'):
        # Method to print the average land size for the specified suburb
        print("\n")
        print("This is the average of the land size:")
        if suburb == 'all':
            for sub in dataframe['suburb'].unique():
                # Print the average land size for each suburb
                print(sub + " Land Size",
                      dataframe.loc[dataframe['suburb'] == sub].loc[dataframe['land_size'] >= 0]['land_size'].mean())
                print("\n")
        else:
            if suburb not in dataframe['suburb'].unique():
                print("No such suburb found.")
                return
            # Print the average land size for the specified suburb
            print(suburb + " Land Size",
                      dataframe.loc[dataframe['suburb'] == suburb].loc[dataframe['land_size'] >= 0]['land_size'].mean())
            print("\n")

    def locate_price(self, target_price, data, target_suburb):
        # Method to locate a specified price and print the result
        if target_suburb not in data['suburb'].unique():
            print("No such suburb found.")
            return
        df = data.loc[data['suburb'] == target_suburb].dropna(subset = ['price'])
        price_list = df['price'].tolist()
        self.reverse_insertion_sort(price_list) # Sort the price list in descending order
        start, end = 0, len(price_list) - 1
        result = self.recursive_binary_search(target_price, price_list, start, end)

        # Print the one of the price list for the reference
        if not result:
            print('\nHere is price list reference.')
            print(int(price_list[0]))
        return result

    def reverse_insertion_sort(self, arr):
        # Method to perform reverse insertion sort
        for end in range(1, len(arr)):
            i = end
            while i > 0 and arr[i - 1] < arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                i -= 1

    def recursive_binary_search(self, target_price, price_list, start, end):
        # Method to perform a recursive binary search
        if start <= end:
            mid = (start + end) // 2
            if float(target_price) < price_list[mid]:
                return self.recursive_binary_search(target_price, price_list, mid + 1, end)
            elif float(target_price) > price_list[mid]:
                return self.recursive_binary_search(target_price, price_list, start, mid - 1)
            elif float(target_price) == price_list[mid]:
                return True
        return False
