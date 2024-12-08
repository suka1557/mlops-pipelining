import os
import pandas as pd
import numpy as np

# Load the data
filepath = os.path.join(os.getcwd(), 'data', 'news.csv')
data = pd.read_csv(filepath)


# define a function to gnerate a random number between 1 to 10
def random_number():
    return np.random.randint(1, 10)

# Generate a date range
dates = pd.date_range(start='1/1/2000', end='1/1/2021', freq='D')

# Create a date list
n = len(data)
index = 0
date_list = []

while len(date_list)  < n:
    no_of_days = random_number()
    date = dates[index].strftime('%Y-%m-%d')
    date_list.extend([date]*no_of_days)

    index += 1

date_list = date_list[:n]

# Add the date list to the data
data['date'] = date_list

# Save the data
data = data[ data.columns[1 : ] ]
data.to_csv(filepath, index=False)
print(data.columns)

#print min and max date in the data
print(data['date'].min(), data['date'].max())