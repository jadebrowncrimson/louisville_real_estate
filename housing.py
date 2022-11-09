import pandas  as pd
import numpy as np

#data import
df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_project.csv')
df.head()

#filter for Louisville zip codes
df = df[df['zip_name'].str.contains('louisville, KY')]

#zip code input
zip_code = input("Enter a zip code ")
print("For zip code" + zip_code + ": ")

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['postal_code'] = pd.to_numeric(df['postal_code'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='postal_code', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the median_listing_price column
house_listing_price = df.loc[df['postal_code'] == int(zip_code)]['median_listing_price'].iloc[0]

print("Average median listing price: ")
print(f"{(house_listing_price):,.2f}")

#mortgage calculator
#down payment = 3.5%
#years = 30
#interest rate = 7.25%
def mortgage_calculator(price):
    down_payment = .035
    principal = price*(1-down_payment)
    interest_monthly = .0725/12
    n = 30*12
    return principal*(interest_monthly*(1 + interest_monthly)**n)/((1+interest_monthly)**n-1)

print("Estimated mortgage payment: ")
print(mortgage_calculator(house_listing_price))

#print(mortgage_calculator(f"{(house_listing_price):,.2f}"))
