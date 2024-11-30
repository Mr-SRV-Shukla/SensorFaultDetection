import os
import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
from src.utils import export_collection_as_dataframe
from src.constant import *
# Assuming the project root is one level above the src directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join(project_root, 'artifacts', 'train.csv')
    test_data_path:str = os.path.join(project_root, 'artifacts', 'test.csv')
    raw_data_path:str = os.path.join(project_root, 'artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        # Initialize the ingestion_config attribute here
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered method of DataIngestion class")
        try:
            df: pd.DataFrame = export_collection_as_dataframe(
                db_name=MONGO_DATABASE_NAME, collection_name=MONGO_COLLECTION_NAME
            )
            logging.info("Exported collection as dataframe")

            # Ensure the directory exists before saving the raw data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Raw data is created')

            # Split data into training and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info('Train data is created')

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Test data is created')

            logging.info(f"Ingested data from mongodb to {self.ingestion_config.raw_data_path}")

            logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error(f"Exception occurred at Data Ingestion Stage: {e}")
            raise CustomException(e, sys)
