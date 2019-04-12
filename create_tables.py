import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    print('='*40)
    print("Create connection")
    conn = psycopg2.connect("host=127.0.0.1 user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    print('-'*40)
    print("Drop then create DB")
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    print('-'*40)
    print("Connect to sparkifydb")
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    print('-'*40)
    print("Drop tables")
    drop_tables(cur, conn)
    print('-'*40)
    print("Create tables")
    create_tables(cur, conn)

    conn.close()
    print('!'*40)
    print("Done !!!")

if __name__ == "__main__":
    main()