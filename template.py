import os 
from pathlib import Path

list_of_files = [
    "QAWithPdf/__init__.py",
    "QAWithPdf/data_ingestion.py",
    "QAWithPdf/embedding.py",
    "QAWithPdf/model_api.py",
    "Experiments/expermient.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # If filedir is not empty then create it if not exists 
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        # logging.info(f"Creating Directory {filedir} for the file {filename}")

    # if filepath does not exist, then make it 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass

    else:
        pass
        # logging.info(f"{filename} is already created")