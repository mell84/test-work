#!/usr/bin/env  python3
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="database",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = 'create database max_db'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

