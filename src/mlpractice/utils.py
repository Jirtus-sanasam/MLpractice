import os 
import sys
from src.mlpractice.exception import CustomException
from src.mlpractice.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")



def read_sql_data():
    logging.info("Reading from mysql database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("Connection to MySQL database established successfully: %s", mydb)
        df = pd.read_sql_query('Select * from churn', mydb)
        return df
    
    except Exception as ex:
        raise CustomException(ex)