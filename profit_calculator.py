
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#HOUSING DATA
#data import
df = pd.read_csv('https://raw.githubusercontent.com/jadebrowncrimson/louisville_real_estate/main/Data/zip_code_data_project.csv')
df.head()

#filter for Louisville, KY zip codes
df = df[df['zip_name'].str.contains('louisville, KY')]


#zip code input
zip_code = input("Enter a zip code in Louisville, KY")
print("For zip code " + zip_code + ": ")

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['postal_code'] = pd.to_numeric(df['postal_code'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='postal_code', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the average_listing_price column
house_listing_price = df.loc[df['postal_code'] == int(zip_code)]['average_listing_price'].iloc[0]

print("Average listing price: ", f"{(house_listing_price):,.2f}")

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
    return principal*((interest_monthly*(1 + interest_monthly)**n)/((1+interest_monthly)**n-1))

print("Estimated mortgage payment: ", f"{mortgage_calculator(house_listing_price):,.2f}")


#RENTAL DATA
# import data
df = pd.read_csv('https://raw.githubusercontent.com/jadebrowncrimson/louisville_real_estate/main/Data/zip_code_data_rentals.csv')
df.head()

# filter for Louisville, KY zip codes
df = df[df['StateName'].str.contains('KY')]
df = df[df['City'].str.contains('Louisville')]

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['RegionName'] = pd.to_numeric(df['RegionName'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='RegionName', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the average_listing_price column
rental_price = df.loc[df['RegionName'] == int(zip_code)]['9/30/2022'].iloc[0]

print("Average rental price: ", f"{(rental_price):,.2f}")

#profit calculator
profit = rental_price - mortgage_calculator(house_listing_price)

print("Estimated monthly profit: ", f"{profit:,.2f}")
