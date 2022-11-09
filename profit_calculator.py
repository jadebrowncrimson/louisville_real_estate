
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

#HOUSING DATA
#data import
df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_project.csv')
df.head()

#filter for Louisville, KY zip codes
df = df[df['zip_name'].str.contains('louisville, KY')]

#zip code input
zip_code = input("Enter a zip code ")
print("For zip code " + zip_code + ": ")

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['postal_code'] = pd.to_numeric(df['postal_code'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='postal_code', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the median_listing_price column
house_listing_price = df.loc[df['postal_code'] == int(zip_code)]['median_listing_price'].iloc[0]

print("Average median listing price: ", f"{(house_listing_price):,.2f}")

# mortgage calculator
# down payment = 3.5%
# years = 30
# interest rate = 7.25%
# n = number of periods it will take to pay off mortgage
def mortgage_calculator(price):
    down_payment = .035
    principal = price*(1-down_payment)
    interest_monthly = .0725/12
    n = 30*12
    return principal*(interest_monthly*(1 + interest_monthly)**n)/((1+interest_monthly)**n-1)

print("Estimated mortgage payment: ", f"{mortgage_calculator(house_listing_price):,.2f}")


#RENTAL DATA
# import data
df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_rentals.csv')
df.head()

# filter for Louisville, KY zip codes
df = df[df['StateName'].str.contains('KY')]
df = df[df['City'].str.contains('Louisville')]

#df.drop(df.loc[:,'3/31/2015':'6/30/2019'].columns, axis=1)

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['RegionName'] = pd.to_numeric(df['RegionName'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='RegionName', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the median_listing_price column
rental_price = df.loc[df['RegionName'] == int(zip_code)]['9/30/2022'].iloc[0]

print("Average rental price as of 10/31/2022: ", f"{(rental_price):,.2f}")

#profit calculator
profit = mortgage_calculator(house_listing_price) - rental_price

print("Estimated monthly profit: ", f"{profit:,.2f}")


xpoints = np.array(df.loc[:,'7/31/2019':'9/30/2022'].columns)
ypoints = np.array(df.loc[df['RegionName'] == int(zip_code)]['9/30/2022'].iloc[0])

plt.plot(xpoints, ypoints)
plt.show()