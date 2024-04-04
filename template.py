import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject"

List_of_file = [
    f"src/{project_name}/init.py",
    f"src/{project_name}/components/init.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/init.py",
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",
    f"src/{project_name}/exception_handling.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "requirements.py",
    "main.py",
    "setup.py",
    "dockerfile"
    
]

for  filepath in List_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")
        
    if(not os.path.exists(filepath)) or (os.Path.getsize(filepath) == 0):
        with open(filepath,'w') as f :
            pass
            logging.info(f"creating empty file : {filepath} ")
            
            
    else: logging.info(f"{filename} is already exist")

