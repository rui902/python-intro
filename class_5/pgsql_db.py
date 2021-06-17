#!/usr/bin/env python3
# coding: utf-8
"""Contains the code necessary to run the airport project using postgres database"""


import psycopg2
import traceback
from psycopg2 import OperationalError, Error


def create_connection(db_user, db_password, db_host, db_port, db_name=None):
    connection = None

    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")

    except OperationalError as e:
        traceback.print_exc()
        raise

    return connection


def run_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("Query executed successfully")

    except OperationalError as oe:
        print("An OperationalError occurred")
        traceback.print_exc()

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


if __name__ == "__main__":
    c = create_connection("postgres", "postgres", "localhost", 5432, "airport")
    c.close()
