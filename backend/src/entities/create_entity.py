import psycopg2
from config import config

def table_create():
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("CREATE TABLE url_shortener(url_id serial PRIMARY KEY, long_url VARCHAR(255), short_url VARCHAR(255));")
        conn.commit()
        print("Table has been created.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    table_create()