from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from QAWithPdf.data_ingestion import load_data
from QAWithPdf.model_api import load_model 
import sys 
from exception import customexception
from logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("Downloading Gemini Embedding Model...")
        gemini_embed_model = GeminiEmbedding(model="models/embedding-001")
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        logging.info("Embedding Model Downloaded Successfully!!")

        logging.info("Making of VectorDatabase in Progress..")
        index = VectorStoreIndex.from_documents(document)
        index.storage_context.persist()
        logging.info("Local Storage made Successfully!!")

        logging.info("Making a query engine")
        query_engine = index.as_query_engine()
        return query_engine
    
    except Exception as e:
        raise customexception(e,sys)