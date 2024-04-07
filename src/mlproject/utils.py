import os
import sys
from src.mlproject.exception_handling import exception_hander
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")



def read_sql_data():
    logging.info("Reading from sql database. ")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection_established ")
        df = pd.read_sql_query('select * from superstore',mydb)
        print(df.head())
        
        return df
        
        
    except Exception as ex:
        raise exception_hander(ex,sys)
    
    