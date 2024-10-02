import pandas as pd
import matplotlib.pyplot as plt
from SimpleDataAnalyser import SimpleDataAnalyser

class DataVisualiser:  # to deal with the visualisations
    def __init__(self):
        # Initialization method for the DataVisualiser class
        # Create an instance of the SimpleDataAnalyser class and assign it to self.sda
        self.sda = SimpleDataAnalyser()

    def prop_val_distribution(self, dataframe, suburb='all', target_currency = 'AUD'):
        # Method to visualize property value distribution
        # Args:
        #   dataframe: DataFrame containing the data to be analyzed
        #   suburb: The area to be analyzed (default is 'all')
        #   target_currency: Currency unit (default is 'AUD')
        currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87,
                         "HKD": 5.12, "KRW": 860.92, "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}

        # Convert the target currency to uppercase
        target_currency = target_currency.upper()
        if suburb == 'all':
            # Iterate over all suburbs if 'all' is set
            for sub in dataframe['suburb'].unique():
                # Extract data for each suburb and remove missing price data
                prices = dataframe.loc[dataframe['suburb'] == sub].dropna(subset = ['price'])
                try:
                    currency = currency_dict[target_currency]
                    # Convert prices in data using the currency exchange method
                    data = self.sda.currency_exchange(prices, currency)['price']

                    # Create a histogram
                    plt.hist(data, alpha = 0.7)

                    # Set graph title and labels
                    plt.title('Property Value Distribution')
                    plt.xlabel(target_currency)
                    plt.ylabel('Properties')

                    # Save the graph as an image file
                    plt.savefig(suburb + '_pvd.png')
                except:
                    print("No such currency found, use 'AUD' as default.")
                    # Call again with 'AUD' currency as default in case of an exception
                    self.prop_val_distribution(dataframe)
        else:
            if suburb not in dataframe['suburb'].unique():
                print("No such suburb found, use 'all' as default.")
                # Call again with 'all' if the specified suburb is not in the DataFrame
                self.prop_val_distribution(dataframe, target_currency = target_currency)
            prices = dataframe.loc[dataframe['suburb'] == suburb].dropna(subset = ['price'])
            try:
                currency = currency_dict[target_currency]
                data = self.sda.currency_exchange(prices, currency)['price']

                # Create a histogram
                plt.hist(data)

                # Set graph title and labels
                plt.title('Property Value Distribution')
                plt.xlabel('Price in ' + target_currency)
                plt.ylabel('Number of properties')

                # Save the graph as an image file
                plt.savefig(suburb + '_pvd.png')
            except:
                print("No such currency found, use 'AUD' as default.")
                # Call again with 'AUD' currency as default in case of an exception
                self.prop_val_distribution(dataframe, suburb)

    def sales_trend(self, dataframe):
        # Method to visualize sales trends
        # Args:
        #   dataframe: DataFrame containing the data to be analyzed
        # Create a new DataFrame 'df' by dropping rows with missing values in the 'sold_date' column
        # from the input 'dataframe'.
        df = dataframe.dropna(subset = ['sold_date'])
        df = df.copy()

        # Convert the 'sold_date' column to a datetime format with the specified date format ("%d/%m/%Y").
        # Extract the year from the 'sold_date' column and store it in a new 'sold_year' column.
        df['sold_date'] = pd.to_datetime(df['sold_date'], format = "%d/%m/%Y")
        df['sold_year'] = df['sold_date'].dt.year

        # Find the unique years present in the 'sold_year' column and store them in the 'years' variable.
        years = df['sold_year'].unique()
        counts = []

        # Iterate through the unique years.
        for year in years:
            # For each year, count the number of properties sold and append the count to the 'counts' list.
            # This counts how many properties were sold in each unique year.
            counts.append(df.loc[df['sold_year'] == year]['sold_year'].count())

        # Create a line graph
        plt.plot(years, counts)
        plt.title('Properties Sold Chart')
        plt.xlabel('Year')
        plt.ylabel('Number')

        # Save the graph as an image file
        plt.savefig('sold.png')
