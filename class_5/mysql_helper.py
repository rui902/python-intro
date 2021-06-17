#!/usr/bin/env python3
# coding: utf-8
"""Just a helper script that will interact with the databases"""

import random
import mysql_db_2 as db
from config import DATABASE_CONFIGS, RANDOM_NAMES, AGES_RANGE


def connect_database(update_config=None):
    config = DATABASE_CONFIGS.get("dev", {}).get("MYSQL", {})

    if update_config is not None and isinstance(update_config, dict):
        config.update(update_config)

    return db.create_connection(**config)


def create_database(connection):
    create_db_query = """CREATE DATABASE IF NOT EXISTS airport CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;"""
    db.run_query(connection, create_db_query)


def drop_table(connection):
    drop_users_table_query = """DROP TABLE IF EXISTS users;"""
    db.run_query(connection, drop_users_table_query)


def create_table(connection):
    create_users_table_query = "CREATE TABLE IF NOT EXISTS users (" \
                               "    id INT PRIMARY KEY AUTO_INCREMENT," \
                               "    name VARCHAR(255) NOT NULL," \
                               "    age INT," \
                               "    gender VARCHAR(20)," \
                               "    nationality VARCHAR(50)" \
                               ");"
    db.run_query(connection, create_users_table_query)


def insert_random_data(connection, num):
    insert_query = "INSERT INTO users(name, age) VALUES(%s, %s);"

    tmp_names = RANDOM_NAMES[:]

    if num > len(tmp_names):
        tmp_names = RANDOM_NAMES*10

    random.shuffle(tmp_names)
    tmp_names = tmp_names[:num]

    ages = [random.randrange(*AGES_RANGE) for _ in tmp_names]

    values = zip(tmp_names, ages)

    db.run_many(connection, insert_query, values)


def search_by_age_normal(connection, age_min):
    search_query = "SELECT id, name, age FROM users WHERE age >= %s;" % age_min
    return db.run_get_query(connection, search_query)


def search_by_age_generator(connection, age_min):
    search_query = "SELECT id, name, age FROM users WHERE age >= %s;" % age_min
    return db.run_generator_get_query(connection, search_query)


def search_by_age_dict(connection, age_min):
    search_query = "SELECT id, name, age FROM users WHERE age >= %s;" % age_min
    return db.run_dict_get_query(connection, search_query)


if __name__ == "__main__":
    # regular database connection; create database; create table; disconnect
    conn = connect_database()
    create_database(conn)
    conn.close()

    print("\n\n")

    # regular database connection but specify which database to connect to; drop and recreate users table
    conn = connect_database({"database": "airport"})
    drop_table(conn)
    create_table(conn)

    print("\n\n")

    # insert pseudo-randomly generated data
    insert_random_data(conn, 50)

    print("\n\n")

    # search using regular cursor
    results = search_by_age_normal(conn, 70)
    print(type(results))
    for r in results:
        print(r)

    print("\n\n")

    # search using generator cursor (SSCursor)
    results2 = search_by_age_generator(conn, 65)
    print(type(results2))
    for r in results2:
        print(r)

    print("\n\n")

    # search using dict cursor
    results3 = search_by_age_dict(conn, 60)
    print(type(results3))
    for r in results3:
        print(r)

    # close the connection, always!
    conn.close()
