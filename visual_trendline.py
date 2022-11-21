import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# housing & rental data import
df_housing = pd.read_csv('https://raw.githubusercontent.com/jadebrowncrimson/louisville_real_estate/main/Data/zip_code_data_project.csv', dtype=str)
df_rentals = pd.read_csv('https://raw.githubusercontent.com/jadebrowncrimson/louisville_real_estate/main/Data/zip_code_data_rentals.csv')


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
print(ypoints)

# show visual
plt.plot(xpoints, ypoints)
plt.show()


