import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# housing & rental data import
df_rentals = pd.read_csv(
    'C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_rentals.csv')
df_housing = pd.read_csv(
    'C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_project.csv', dtype=str)

#filter for Louisville, KY zip codes as of 9/30/2022
df_housing = df_housing[df_housing['zip_name'].str.contains('louisville, KY')]
df_housing = df_housing[df_housing['month_date_yyyymm'].str.contains('202209')]

#PIE CHART
#pie chart that shows how various zip code housing prices compare
y = np.array(df_housing['average_listing_price'])
labels = np.array(df_housing['postal_code'])

plt.pie(y, labels = labels)
plt.show() 

#TRENDLINE
# input
zip_code = input("Enter a zip code in Louisville, KY")

# filter for zip code input
df_housing = df_housing[df_housing['postal_code'].str.contains(zip_code)]

# cast to numeric
df_housing['average_listing_price'] = pd.to_numeric(
    df_housing['average_listing_price'], errors='coerce')
df_housing['month_date_yyyymm'] = pd.to_datetime(
    df_housing['month_date_yyyymm'], format="%Y%m", errors='coerce')

# average median listing prices trend
xpoints = np.array(df_housing['month_date_yyyymm'])
ypoints = np.array(df_housing['average_listing_price'])

# show visual
plt.plot(xpoints, ypoints)
plt.show()


