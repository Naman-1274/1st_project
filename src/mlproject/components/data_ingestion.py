import os
import sys
from src.mlproject.exception_handling import exception_hander
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('Data_paths','train_csv')
    test_data_path:str=os.path.join('Data_paths','test_csv')
    raw_data_path:str=os.path.join('Data_paths','raw_csv')
    
class dataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def start_data_ingestion(self):
        try:
            df=read_sql_data()
            logging.info("reading completed mysql database. ")
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data ingestion is complete.")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
            
        except Exception as e:
            raise exception_hander(e,sys)

