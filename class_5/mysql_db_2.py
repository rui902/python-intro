#!/usr/bin/env python3
# coding: utf-8
"""Contains the code necessary to run the airport project using mysql database, MySQLdb library"""

import traceback
from MySQLdb import Connection, Error
from MySQLdb.cursors import SSCursor, DictCursor


def create_connection(*args, **kwargs):
    print(kwargs)

    if not kwargs:
        raise ValueError("Must send connection details")

    if not kwargs.get("host", None) or not kwargs.get("user", None) or not kwargs.get("passwd", None):
        raise ValueError("Arguments 'host', 'user' and 'passwd' are required")

    connection = None

    try:
        connection = Connection(
            host=kwargs.get("host", None),
            user=kwargs.get("user", None),
            passwd=kwargs.get("passwd", None),
            database=kwargs.get("database", "mysql")
        )
        print("Connection to MySQL DB successful")

    except Error as e:
        traceback.print_exc()
        raise

    return connection


def run_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()  # save
        print("Query: OK")

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


def run_many(connection, query, values):
    cursor = connection.cursor()

    try:
        cursor.executemany(query, values)
        connection.commit()
        print("Query: OK")

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


def run_get_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)

        for row in cursor:
            yield row

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


def run_generator_get_query(connection, query):
    """Ultra-efficient cursor for huge amounts of data"""

    cursor = SSCursor(connection)

    try:
        cursor.execute(query)
        for row in cursor:
            yield row

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


def run_dict_get_query(connection, query):
    cursor = DictCursor(connection)

    try:
        cursor.execute(query)
        for row in cursor:
            yield row

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


if __name__ == "__main__":
    c = create_connection(
        host="localhost",
        user="root",
        passwd="qwerty123...",
        # database="airport"
    )

    # uncomment for purposeful error - just testing traceback output
    # run_query(c, "INSERT x")

    c.close()
