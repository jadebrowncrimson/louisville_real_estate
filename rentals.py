import pandas  as pd

df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_rentals.csv')
df.head()

df = df[df['StateName'].str.contains('KY')]
df = df[df['City'].str.contains('Louisville')]

df.drop(df.loc[:,'3/31/2015':'6/30/2019'].columns, axis=1)

#calculator
#zip code input
zip_code = input("Enter a zip code ")

# cast the postal code column to numeric type ('coerce' means convert any invalid cells to NaN)
df['RegionName'] = pd.to_numeric(df['RegionName'], errors='coerce')

# drop any values from the postal code column that are NaN or None
df.dropna(axis=0, subset='RegionName', inplace=True)

# find the row where postal_code equals the user's input, then read the value of the median_listing_price column
rental_price = df.loc[df['RegionName'] == int(zip_code)]['9/30/2022'].iloc[0]

print (f"{(rental_price):,.2f}")