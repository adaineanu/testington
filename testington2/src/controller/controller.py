from validate_email import validate_email

from database.libPG import LibPG
from config import db_params


class TestingtonController(object):
    def __init__(self):
        self.__libPG = LibPG(db_params)

    def insert_row(self, email, message=''):
        """
        Inserts row into database using database library

        :param email: unvalidated email
        :param message: message string
        :return: Info about what happened
        """
        if validate_email(email) is False:
            return "Email is not valid"
        return self.__libPG.insert_row(email, message)

    def get_rows(self):
        """
        Returns 10 entries from database library

        :return: list of entries
        """
        return self.__libPG.get_rows(how_many=10)


if __name__ == '__main__':
    print(validate_email('example@example.com'))
