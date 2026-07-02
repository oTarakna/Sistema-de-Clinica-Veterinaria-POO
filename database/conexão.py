import os
import psycopg2
from contextlib import contextmanager

class DBConnection:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "vetsys_db")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASS = os.getenv("DB_PASS", "172236")
    DB_PORT = os.getenv("DB_PORT", "5432")

    @classmethod
    @contextmanager
    def get_cursor(cls):
        conn = None
        try:
            conn = psycopg2.connect(
                host=cls.DB_HOST,
                database=cls.DB_NAME,
                user=cls.DB_USER,
                password=cls.DB_PASS,
                port=cls.DB_PORT
            )
            cursor = conn.cursor()
            yield cursor
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise RuntimeError(f"Falha operacional no Banco de Dados: {e}")
        finally:
            if conn:
                conn.close()
