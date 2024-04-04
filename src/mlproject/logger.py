import logging
import os
from datetime import datetime

Log_file=f"{datetime.now().strftime('%d,%m,%Y,%H,%M,%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",Log_file)
os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,Log_file)

logging.basicConfig(
    filename=log_file_path, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

