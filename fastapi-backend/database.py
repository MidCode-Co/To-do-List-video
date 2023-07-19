import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=f"password",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("connected to database")
        break
    except Exception as error:
        print("connection to databse failed")
        print(error)
        time.sleep(2)