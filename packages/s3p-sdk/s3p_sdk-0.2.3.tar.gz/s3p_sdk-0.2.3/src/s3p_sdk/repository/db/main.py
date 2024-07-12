import os

import psycopg2

USERNAME = os.getenv('S3P_DATABASE_USERNAME')
HOST = os.getenv('S3P_DATABASE_HOST')
PORT = os.getenv('S3P_DATABASE_PORT')
DATABASE = os.getenv('S3P_DATABASE_DATABASE')
PASSWORD = os.getenv('S3P_DATABASE_PASSWORD')


def ps_connection():
    """
    Create a connection to the PostgreSQL Control-database by psycopg2
    :return:
    """
    return psycopg2.connect(
        database=DATABASE,
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
