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
ENV = os.getenv("ENV", "local")
MONGO_DB_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_DB_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "news")
if ENV == "local":
    MONGO_URI = f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}"
    print(f"Mongo URI: {MONGO_URI}")
else:
    MONGO_SERVICE_NAME = os.getenv("MONGO_SERVICE_NAME", "mongodb1")
    MONGO_URI = f"mongodb://{MONGO_SERVICE_NAME}:{MONGO_DB_PORT}"
    print(f"Mongo URI: {MONGO_URI}")

# MONGO COllection
FAKE_NEWS_COLLECTION_NAME = 'fake-news'
FAKE_NEWS_COLLECTION_UPDATE_DATE = 'fake-news-update-date'
