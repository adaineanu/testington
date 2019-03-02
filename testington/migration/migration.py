import psycopg2
from psycopg2 import sql

db_params = {
    'DB_HOST': "db",
    'DB_PORT': 5432,
    'DB_NAME': "postgres",
    'DB_USER': "postgres",
    'DB_PASSWORD': "postgres"
}

if __name__ == '__main__':
    print("Migration...")
    database = psycopg2.connect(
        host=db_params['DB_HOST'],
        port=db_params['DB_PORT'],
        dbname=db_params['DB_NAME'],
        user=db_params['DB_USER'],
        password=db_params['DB_PASSWORD'])

    with database.cursor() as cursor:
        try:
            cursor.execute(sql.SQL('''
                DROP TABLE testington;'''))
        except psycopg2.ProgrammingError:
            database.rollback()
        try:
            cursor.execute(sql.SQL('''
                CREATE TABLE testington(
                    id BIGSERIAL CONSTRAINT PK_testington PRIMARY KEY,
                    created_at timestamp NOT NULL,
                    message char(255),
                    email char(100) NOT NULL);'''))
            cursor.execute(sql.SQL('''CREATE INDEX idx_email ON testington USING btree(email)'''))
            database.commit()
        except psycopg2.ProgrammingError:
            database.rollback()
