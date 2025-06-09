from dotenv import load_dotenv
load_dotenv()
import os
from sqlalchemy import create_engine

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}".format(
            user=os.getenv("DB_USER", "root"),
            pwd=os.getenv("DB_PASSWORD", "myPassword"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "3306"),
            db=os.getenv("DB_NAME", "clean_database")
        )
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        return create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine