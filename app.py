from src.mlpractice.logger import logging
from src.mlpractice.exception import CustomException
from src.mlpractice.components.data_ingestion import DataIngestion
from src.mlpractice.components.data_ingestion import DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")
    try:
        # DataIngestionConfig= DataIngestionConfig()
        DataIngestion= DataIngestion()
        DataIngestion.initiate_data_ingestion()
        pass
    except Exception as e:
        raise CustomException(e, sys)
