import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# housing & rental data import
df_housing = pd.read_csv('https://raw.githubusercontent.com/jadebrowncrimson/louisville_real_estate/main/Data/zip_code_data_project.csv', dtype=str)

#filter for Louisville, KY zip codes as of 9/30/2022
df_housing = df_housing[df_housing['zip_name'].str.contains('louisville, KY')]
df_housing = df_housing[df_housing['month_date_yyyymm'].str.contains('202209')]

#PIE CHART
#pie chart that shows how various zip code housing prices compare
y = np.array(df_housing['average_listing_price'])
labels = np.array(df_housing['postal_code'])

plt.pie(y, labels = labels)
plt.show() 

