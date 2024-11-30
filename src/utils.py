import os 
import sys
import boto3
import dill
import numpy as np 
import pandas as pd 
from src.exception import CustomException

from pymongo import MongoClient

#  mongo db data base 
from urllib.parse import quote_plus

def export_collection_as_dataframe(collection_name, db_name):
    try:
        # Original credentials
        username = os.getenv("MONGO_DB_USERNAME")
        password = os.getenv("MONGO_DB_PASSWORD")
        
        # Encode the username and password
        encoded_username = quote_plus(username)
        encoded_password = quote_plus(password)
        
        # Construct the MongoDB connection string with encoded credentials
        client_url = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.qkxzk.mongodb.net/?retryWrites=true&w=majority"
        
        mongo_client = MongoClient(client_url)

        collection = mongo_client[db_name][collection_name]

        df = pd.DataFrame(list(collection.find()))

        if "_id" in df.columns.to_list():
            df = df.drop(columns=["_id"], axis=1)

        df.replace({"na": np.nan}, inplace=True)

        return df

    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)