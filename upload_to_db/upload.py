from database_connect import mongo_operation as mongo
import os
from urllib.parse import quote_plus

# Encode credentials
username = "souravshukla985"
password = "Mahakal@@@1999"
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# MongoDB connection string
client_url = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.qkxzk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
database_name = "sensor"

# Path to the 'content' directory (relative path)
datasets_dir_name = os.path.join(os.path.dirname(__file__), "content")

def upload_files_to_mongodb(mongo_client_con_string, database_name, datasets_dir_name):
    # Ensure the directory exists
    if not os.path.exists(datasets_dir_name):
        raise FileNotFoundError(f"Directory not found: {datasets_dir_name}")

    for file in os.listdir(datasets_dir_name):
        if file.endswith('.csv'):
            file_name = file.split('.')[0]
            file_path = os.path.join(datasets_dir_name, file)
            
            # Establish MongoDB connection
            mongo_connection = mongo(
                client_url=mongo_client_con_string,
                database_name=database_name,
                collection_name=file_name
            )
            
            try:
                # Insert data into MongoDB
                mongo_connection.bulk_insert(file_path)
                print(f"{file_name} is uploaded to MongoDB")
            except Exception as e:
                print(f"Failed to upload {file_name}: {e}")

# Call the function
upload_files_to_mongodb(
    mongo_client_con_string=client_url,
    database_name=database_name,
    datasets_dir_name=datasets_dir_name
)
