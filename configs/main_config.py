import os
from dotenv import load_dotenv

PROJECT_ROOT = os.getcwd()

#Train config path
train_config_path = os.path.join(PROJECT_ROOT,'configs', 'train_configs.yaml')

# CSV file path
news_csv_file_path = os.path.join(PROJECT_ROOT, 'data', 'news.csv')

# Load environment variables
load_dotenv()