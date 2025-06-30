from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_database():
   CONNECTION_STRING = os.getenv("DB_STRING")
   client = MongoClient(CONNECTION_STRING)
 
   return client
  
if __name__ == "__main__":   
     dbname = get_database()
