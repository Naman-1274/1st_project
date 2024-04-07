from src.mlproject.logger import logging
from src.mlproject.exception_handling import exception_hander
import sys
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_ingestion import dataIngestion


if __name__=="__main__":
    logging.info("the execution has satrted")
 
    try:
        # DataIngestionConfig = DataIngestionConfig()
        dataIngestion = dataIngestion()
        dataIngestion.start_data_ingestion()
        
    except Exception as e:
        logging.info("exceptions")
        raise exception_hander(e,sys)        
        
    