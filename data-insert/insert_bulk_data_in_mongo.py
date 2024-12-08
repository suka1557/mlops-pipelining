from pymongo import MongoClient
import pandas as pd
import yaml
import sys
import time

sys.path.append('./')

from configs.main_config import (
    train_config_path, news_csv_file_path,
    MONGO_URI, MONGO_DB_NAME, FAKE_NEWS_COLLECTION_NAME,
    FAKE_NEWS_COLLECTION_UPDATE_DATE
)

# get the cutoff date
def get_date_from_config_yaml(filepath):
    #Read the yaml config file
    config = yaml.safe_load(open(filepath   ))
    cutoff_date = config['data-push-date']
    print(cutoff_date)
    return cutoff_date

# read the csv file
def read_csv_file(filepath):
    news_data = pd.read_csv(filepath)
    print("Data read from csv file")
    return news_data

# filter news based on train cutoff date
def filter_news(news_data, cutoff_date):
    news_data = news_data[news_data['date'] <= cutoff_date]
    print("Data filtered based on cutoff date and comverted to json")

    news_json = news_data.to_dict(orient='records')
    print("Got json with no of records: ", len(news_json))

    return news_json   

def load_data_in_mongo(uri, db, collection, news_json):
    print(f"Connecting to Mongo database: {uri}")
    #Create connection
    client = MongoClient(uri)
    collection = client[db][collection]
    
    # Drop the collection if it exists
    if collection.count_documents({}) > 0:
        collection.drop()  # Drop the collection if it exists

    # Insert data into the collection
    collection.insert_many(news_json)
    print(f"Data inserted into {collection} in Mongo database.")

    # Close the connection
    client.close()

#update date in update collection in mongo
def update_date_in_mongo(uri, db, collection, date):
    print(f"Connecting to Mongo database: {uri}")
    #Create connection
    client = MongoClient(uri)
    collection = client[db][collection]
    
    # Drop the collection if it exists
    if collection.count_documents({}) > 0:
        collection.drop()  # Drop the collection if it exists

    # Insert data into the collection
    collection.insert_one({'last_added_date': date, 'updated_timestamp': int(time.time())})
    print(f"Date updated into {collection} in Mongo database.")

    # Close the connection
    client.close()


# create a function to call all the functions
def main():
    cutoff_date = get_date_from_config_yaml(train_config_path)
    news_data = read_csv_file(news_csv_file_path)
    news_json = filter_news(news_data, cutoff_date)

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
        date=cutoff_date
    )

if __name__ == "__main__":
    main()