from os import remove
from sqlite3.dbapi2 import Error
import database as db
import sqlite3 as sql

def authenticate(auth_data:tuple):
    auth = False
    conn = sql.connect('database/users.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM users WHERE email=? AND password=?''', auth_data)
    if cur.fetchone():
        auth = True
    conn.close()
    return auth

def add_user(new_user_name:str, new_user_password:str):
    user = 'None'
    user_to_add_data = (new_user_name, new_user_password)
    conn = sql.connect('database/users.db')
    cur = conn.cursor()
    user_check = cur.execute('SELECT email FROM users WHERE email=?', (new_user_name,))
    if not user_check.fetchone():
        cur.execute('''INSERT INTO users(email, password) VALUES(?, ?)''', user_to_add_data)
        conn.commit()
        new_user_id = cur.execute('SELECT id FROM users WHERE email=?', (new_user_name,))
        user = f'added a new user with email {new_user_name}'
    else:
        user = 'the email already exists'
    conn.close()

    return user

def delete_user(username, password, remove_user):
    deleted_user = 'None'
    auth_data = (username, password)
    auth = authenticate(auth_data)
    if auth is True:
        conn = sql.connect('database/users.db')
        cur = conn.cursor()
        try:
            user_to_delete_id = cur.execute('SELECT id FROM users WHERE email=?', (remove_user,))
            cur.execute('DELETE FROM users WHERE email=?', (remove_user,))
            conn.commit()
            deleted_user = f'{remove_user} was successfully removed from authenticated users by the {username}'
        #     return deleted_user
        except Error as e:
            print(e)
        conn.close()
    else:
        deleted_user = 'authentication failed'
    return deleted_user

def change_pswd(username, password, new_pswd):
    password_changed = False
    auth_data = (username, password)
    auth = authenticate(auth_data)
    if auth is not None:
        conn = sql.connect('database/users.db')
        cur = conn.cursor()
        try:
            user_id = cur.execute('SELECT id FROM users WHERE email=?', (username,))
            cur.execute('''UPDATE users SET password=? WHERE email=? AND password=?''', (new_pswd, username, password))
            conn.commit()
            password_changed = f'password succefully changed for {username}'
            return password_changed
        except Error as e:
            print(e)
        conn.close()
    else:
        password_changed = 'authentication failed'
    return password_changed

if __name__ == "__main__":
    user = add_user('admin', 'admin', 'admin4', 'admin3')
    print(user)