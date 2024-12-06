import os
from dotenv import load_dotenv

PROJECT_ROOT = os.getcwd()

#Train config path
train_config_path = os.path.join(PROJECT_ROOT,'configs', 'train_configs.yaml')

# CSV file path
news_csv_file_path = os.path.join(PROJECT_ROOT, 'data', 'news.csv')

# Load environment variables
load_dotenv()

# Mongo DB details
MONGO_DB_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_DB_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "news")
MONGO_URI = f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}"

# MONGO COllection
FAKE_NEWS_COLLECTION_NAME = 'fake-news'
