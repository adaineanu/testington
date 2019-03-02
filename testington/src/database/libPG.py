import datetime
import psycopg2

from psycopg2 import sql

# from src import log_exceptions
from database import logger


class LibPG(object):
    def __init__(self, db_params):
        self.__database = psycopg2.connect(
            host=db_params['DB_HOST'],
            port=db_params['DB_PORT'],
            dbname=db_params['DB_NAME'],
            user=db_params['DB_USER'],
            password=db_params['DB_PASSWORD'])
        self.__cursor = None

    def insert_row(self, email, message=''):
        """
        Inserts a new row into table "testington" from database.

        testington(
            id integer,
            created_at timestamp,
            message char[255],
            email char[255]
        )

        :param email: email field of the row, validated
        :param message: message field of the row, can be empty
        :return: info message
        """
        logger.info("Inserting email={0} message={1}".format(email, message))
        self.__cursor = self.__database.cursor()
        self.__cursor.execute(
            sql.SQL('''INSERT INTO testington(created_at, message, email) 
                VALUES({created_at}, {message}, {email}) RETURNING id;''').format(
                    created_at=sql.Literal(datetime.datetime.now()),
                    message=sql.Literal(message),
                    email=sql.Literal(email)
            )
        )
        self.__database.commit()
        self.__cursor.close()
        logger.info("Inserted successfully")
        return "Inserted entry successfully"

    def get_rows(self, how_many=10):
        """
        Queries the database to get entries from table "testington".

        :param how_many: how many entries to retrieve from the table
        :return: a dict composed from the entries in the database
        """
        logger.info("Getting top 100 rows")
        self.__cursor = self.__database.cursor()
        self.__cursor.execute(
            sql.SQL('''SELECT id, created_at, message, email FROM testington LIMIT {how_many};''').format(
                how_many=sql.Literal(how_many)
            )
        )
        data = self.__cursor.fetchall()
        self.__cursor.close()
        return [{"id": i[0],
                 "created_at": i[1],
                 "message": i[2],
                 "email": i[3]}
                for i in data]


if __name__ == '__main__':
    print(datetime.datetime.now())
