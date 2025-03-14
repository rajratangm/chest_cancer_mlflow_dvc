import os 
from pathlib import Path 
import logging 

logging.basicConfig(Level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'
            

list_of_files = [
".github/workflows/.gitkeep",
f"src/{project_name}/_init _. py",
f"src/{project_name}/components/_init _. py",
f"src/{project_name}/utils/_init _. py",
f"src/{project_name}/config/_init _. py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/_init _. py",
f"src/{project_name}/entity/_init _. py",
f"src/{project_name}/constants/_init _. py",
"config/config.yaml",
"dvc.yaml",
"params.yaml",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory; {filedir} for the file :{filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass 
            logging.info(f'creating empty file:')
