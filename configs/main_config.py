import os
from dotenv import load_dotenv

PROJECT_ROOT = os.getcwd()

#Train config path
train_config_path = os.path.join(PROJECT_ROOT,'configs', 'train_configs.yaml')

# CSV file path
news_csv_file_path = os.path.join(PROJECT_ROOT, 'data', 'news.csv')

# Load environment variables
load_dotenv()

# Mongo DB credentials
MONGO_DB_USERNAME = os.getenv("MONGO_USERNAME", "admin")
MONGO_DB_PASSWORD = os.getenv("MONGO_PASSWORD", "password")
MONGO_DB_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_DB_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "news")
MONGO_URI = f"mongodb://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}"

# MONGO COllection
FAKE_NEWS_COLLECTION_NAME = 'fake-news'
