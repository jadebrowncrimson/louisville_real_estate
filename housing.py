import pandas  as pd
import numpy as np

#data import
df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_project.csv')
df.head()

#filter for Louisville zip codes
df = df[df['zip_name'].str.contains('louisville, KY')]

#zip code input
zip_code = input("Enter a zip code ")

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['postal_code'] = pd.to_numeric(df['postal_code'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='postal_code', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the median_listing_price column
house_listing_price = df.loc[df['postal_code'] == int(zip_code)]['median_listing_price'].iloc[0]

print(f"{(house_listing_price):,.2f}")

