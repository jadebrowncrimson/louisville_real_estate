import pandas  as pd

df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_owned_homes.csv')
df.head()

df = df[df['StateName'].str.contains('KY')]
df = df[df['City'].str.contains('Louisville')]

df.drop(df.loc[:,'3/31/2015':'6/30/2019'].columns, axis=1)

print (df)