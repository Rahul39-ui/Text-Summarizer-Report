import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "textSummarizer"

list_of_files = [
    #will help us deploy to github
    ".github/workflows/.gitkeep",
    #if we want to install as local package the local package will be considered
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    #seperate folder and file so split
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        #exist_ok = True will check for existence of the file and return True if it exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
            
    else:
        logging.info(f"{filename} already exists")
         
        
        
        
        
