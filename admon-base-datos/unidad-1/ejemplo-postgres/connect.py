# coding: utf-8
import psycopg2
from config import config


def connect():
    """
        Conecta con la base de datos del servidor.
    """
    conn = None
    try:
        # lee los parámetros de la conexión.
        params = config()

        # conecta con el server de PostgreSQL.
        print("Conectando con la base de datos de PostgreSQL")
        conn = psycopg2.connect(**params)

        # crear un cursor.
        cur = conn.cursor()

        # ejecuta una declaración.
        print("versión de la base de datos de PostgreSQL: ")
        cur.execute("SELECT version()")

        # muestra la versión del servidor de base de datos PostgreSQL.
        db_version = cur.fetchone()
        print(db_version)

        # cierra la comunicación con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()