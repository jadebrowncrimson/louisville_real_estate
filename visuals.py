import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_rentals.csv')

zip_code = input("Enter a zip code")

xpoints = np.array(df.loc[:,'7/31/2019':'9/30/2022'].columns)
ypoints = np.array(df.loc[df['RegionName'] == int(zip_code)]['9/30/2022'].iloc[0])

plt.plot(xpoints, ypoints)
plt.show()