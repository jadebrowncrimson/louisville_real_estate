import pandas  as pd

df = pd.read_csv('C:/Users/Jade/OneDrive - University of Louisville/Handling Business/Trainings/Code Louisville Python/Code/final_project/Data/zip_code_data_project.csv')
df.head()

df = df[df['zip_name'].str.contains('louisville, KY')]

print (df)
