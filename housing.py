import pandas  as pd
import numpy as np

#data import
df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_project.csv')
df.head()

#filter for Louisville zip codes
df = df[df['zip_name'].str.contains('louisville, KY')]

#calculator
#zip code input
zip_code = input("Enter a zip code ")

#casted postal_code to string
series = df['postal_code']
df['postal_code'] = df['postal_code'].astype(str)
df = df[df['postal_code'].str.contains(zip_code)]

print(type(df))

#retrieve median listing price
#retrieve row index by referencing zip code


average_listing_price = df['median_listing_price'].iloc[df['postal_code'].str.contains(zip_code)]

#print average listing price
print (average_listing_price)

#print ("Average listing price: " + df[''])