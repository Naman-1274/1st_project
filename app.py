from src.mlproject.logger import logging
from src.mlproject.exception_handling import exception_hander
import sys


if __name__=="__main__":
    logging.info("the execution has satrted")
 
    try:
        1/0
    except Exception as e:
        logging.info("exceptions")
        raise exception_hander(e,sys)        
        
    