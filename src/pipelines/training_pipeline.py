import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../")))
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
from src.components.data_ingestion import DataIngestion


if __name__=="__main__":
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)