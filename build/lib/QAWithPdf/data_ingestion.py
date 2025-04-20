from llama_index.core import SimpleDirectoryReader
import sys 
from exception import customexception
from logger import logging

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
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("Data Loaded Successfully!!")
        return documents
    except Exception as e:
        raise customexception(e,sys)
    