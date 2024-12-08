import pandas as pd
import json
import os
import yaml

# Read the CSV file
filepath = os.path.join(os.getcwd(), 'data', 'news.csv')
json_filepath = os.path.join(os.getcwd(), 'data', 'news.json')

# Read the CSV file
df = pd.read_csv(filepath)
print(f"Data shape: {df.shape}")

#Read cutoff date from yaml config file
cutoff_date_config_filepath = os.path.join(os.getcwd(),'configs' ,'train_configs.yaml')
config = yaml.safe_load(open(cutoff_date_config_filepath))
cutoff_date = config['data-push-date']

# Filter the data
df = df[df['date'] <= cutoff_date]
print(f"Data shape: {df.shape}")

# Convert the DataFrame to a dictionary
json_data = df.to_dict(orient='records')

# Save the dictionary to a JSON file
with open(json_filepath, 'w') as f:
    json.dump(json_data, f)