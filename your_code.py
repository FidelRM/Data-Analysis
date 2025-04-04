import pandas as pd

# Uploading dataframe 
df = pd.read_csv('GoogleApps.csv')


# What is the name of the first application containing in the dataset?
result = df.head(1)
print(result)


# What is the category of the last application containing in the dataset?
print(df.tail(1))


# How many columns are there in the dataset?
df.describe()
# What is the type of data stored in each column?


# Specify the arithmetic mean and median for the size of the applications.
# How much does the most expensive application cost?
# *Specify the arithmetic mean and median for the number of application installs.
