from llama_index.core import SimpleDirectoryReader
import os
import sys 
from exception import customexception
from logger import logging
import tempfile

def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data(str): The path to the directory containing PDF File.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """

    try:
        logging.info("Data Loading Started...")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, data.name)
            with open(file_path, "wb") as f:
                f.write(data.read())

            loader = SimpleDirectoryReader(input_dir=temp_dir)
            documents = loader.load_data()

        logging.info("Data Loaded Successfully!!")
        return documents
    except Exception as e:
        raise customexception(e,sys)
    