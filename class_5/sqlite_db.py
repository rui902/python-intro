#!/usr/bin/env python3
# coding: utf-8
"""Contains the code necessary to run the airport project using sqlite database"""

import sqlite3
import traceback
from sqlite3 import Error


def create_connection(path):
    connection = None

    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")

    except Error as e:
        traceback.print_exc()
        raise

    return connection


def run_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")

    except Error as e:
        print("An error occurred")
        traceback.print_exc()


if __name__ == "__main__":
    c = create_connection("./sqlite_airport.db")

    q = """CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      gender TEXT,
      nationality TEXT
    );"""
    run_query(c, q)

    c.close()
