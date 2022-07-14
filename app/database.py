import sqlite3 as sql
from sqlite3 import Error
from sqlite3.dbapi2 import Connection, Cursor

def dbconnect(db_file):
    # '''create a database connection'''
    conn = None
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
    
def insert_table_data(conn, sql, data):
    cur = conn.cursor()
    try:
        cur.execute(sql, data)
        conn.commit()
    except Error as e:
        print(e)    

def create_table(conn, table):
    # '''create table in the database'''
    try:
        cur = conn.cursor()
        cur.execute(table)
    except:
        print('problem creating table')

if __name__ == "__main__":
    table = '''CREATE TABLE IF NOT EXISTS users(
                id integer PRIMARY KEY,
                email text NOT NUll,
                password text NOT NUll);
                '''
    conn = dbconnect('database/users.db')
    with conn:
        if conn is not None:
            create_table(conn, table)
            print('table created')
