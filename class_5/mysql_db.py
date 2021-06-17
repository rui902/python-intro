#!/usr/bin/env python3
# coding: utf-8
"""Contains the code necessary to run the airport project using mysql database, mysql-connector-python library"""

import mysql.connector
import traceback
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name=None):
    connection = None

    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")

    except Error as e:
        traceback.print_exc()
        raise

    return connection


def run_query(connection, query):
    cursor = connection.cursor()

    try:
        print("Running query:")
        print(query)
        print("")
        cursor.execute(query)
        connection.commit()
        print("Query: OK\n\n")

    except Error as e:
        print("An Error occurred")
        traceback.print_exc()


if __name__ == "__main__":
    conn = create_connection("localhost", "root", "qwerty123...")

    create_db_query = """CREATE DATABASE IF NOT EXISTS airport CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;"""
    run_query(conn, create_db_query)

    conn.close()

    conn = create_connection("localhost", "root", "qwerty123...", "airport")

    drop_users_table_query = """DROP TABLE IF EXISTS users;"""
    run_query(conn, drop_users_table_query)

    create_users_table_query = """CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        age INT,
        gender VARCHAR(20),
        nationality VARCHAR(50)
    );"""
    run_query(conn, create_users_table_query)

    conn.close()
