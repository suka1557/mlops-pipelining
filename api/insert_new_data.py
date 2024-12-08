from fastapi import FastAPI
import sys

sys.path.append('./')

from configs.main_config import (
    news_csv_file_path,
    MONGO_URI, MONGO_DB_NAME, FAKE_NEWS_COLLECTION_NAME,
    FAKE_NEWS_COLLECTION_UPDATE_DATE
)
from modules.databases.mongo.get_mongo_connection import create_connection_to_mongo_server
from data_insert.insert_bulk_data_in_mongo import (
    read_csv_file, filter_news, load_data_in_mongo, update_date_in_mongo
)

app = FastAPI()

@app.get("/last_update_date")
def get_last_update_date_from_mongo(collection=FAKE_NEWS_COLLECTION_UPDATE_DATE):

    client, collection = create_connection_to_mongo_server(
        uri=MONGO_URI,
        db=MONGO_DB_NAME,
        collection=collection
    )

    last_update_date = collection.find_one({}, {'last_added_date': 1})['last_added_date']
    client.close()

    return last_update_date

@app.post("/insert_data_given_date")
def insert_data_in_mongo(insert_date:str):
    news_data = read_csv_file(news_csv_file_path)
    news_json = filter_news(news_data, insert_date)

    load_data_in_mongo(
        uri=MONGO_URI,
        db=MONGO_DB_NAME,
        collection=FAKE_NEWS_COLLECTION_NAME,
        news_json=news_json
    )

    update_date_in_mongo(
        uri=MONGO_URI,
        db=MONGO_DB_NAME,
        collection=FAKE_NEWS_COLLECTION_UPDATE_DATE,
        date=insert_date
    )
    
    return {"message": "Data inserted successfully"}