import logging


class Database:

    @staticmethod
    async def connect():
        print("iniciando db")
        logging.info("Connecting to database")
