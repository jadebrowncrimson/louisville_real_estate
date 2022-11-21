import pandas as pd
from statistics import mean

#data import
df_houses = pd.read_csv('https://github.com/jadebrowncrimson/louisville_real_estate/blob/main/Data/zip_code_data_project.csv')
df_rentals = pd.read_csv('https://github.com/jadebrowncrimson/louisville_real_estate/blob/main/Data/zip_code_data_rentals.csv')

#filter for Louisville houses & rentals
df_houses = df_houses[df_houses['zip_name'].str.contains('louisville, KY')]
df_rentals = df_rentals[df_rentals['StateName'].str.contains('KY')]
df_rentals = df_rentals[df_rentals['City'].str.contains('Louisville')]


#zip codes w/ highest & lowest average housing price
max_house = max(df_houses['average_listing_price'])
max_house_zip = df_houses.loc[df_houses['average_listing_price'] == int(max_house)]['postal_code'].iloc[0]
print("Zip code", max_house_zip, "has the highest average housing price, which is ", f"{(max_house):,.2f}")

min_house = min(df_houses['average_listing_price'])
min_house_zip = df_houses.loc[df_houses['average_listing_price'] == int(min_house)]['postal_code'].iloc[0]
print("Zip code", min_house_zip, "has the lowest average housing price, which is ", f"{(min_house):,.2f}")

#gap in price b/t max and min housing prices
housing_price_gap = max_house - min_house
print("Range between housing max & min: ", f"{(housing_price_gap):,.2f}")

average_house_price = mean(df_houses['average_listing_price'])

print("Average housing price: ", f"{(average_house_price):,.2f}", '\n')

#zip codes w/ highest & lowest average median apartment price
max_rental = max(df_rentals['9/30/2022'])
max_rental_zip = df_rentals.loc[df_rentals['9/30/2022'] == max_rental]['RegionName'].iloc[0]
print("Zip code", max_rental_zip, "has the highest average rental price, which is ", f"{(max_rental):,.2f}")

min_rental = min(df_rentals['9/30/2022'])
min_rental_zip = df_rentals.loc[df_rentals['9/30/2022'] == min_rental]['RegionName'].iloc[0]
print("Zip code", min_rental_zip, "has the lowest average rental price, which is ", f"{(min_rental):,.2f}")


rental_price_gap = max_rental - min_rental
print("Range between rental max & min: ", f"{(rental_price_gap):,.2f}")


