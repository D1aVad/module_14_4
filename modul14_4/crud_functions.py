import re
import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Product(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL)
        '''
    )
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',
        (username, email, age)
    )
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM Users WHERE username = ?', (username, ))
    result = bool(cursor.fetchone())
    connection.close()
    return result


def get_all_products():
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Product')
    result = cursor.fetchall()
    connection.close()
    return result


def post_products():
    connection = sqlite3.connect('telegram_db.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute(
            "INSERT INTO Product (title, description, price) VALUES (?, ?, ?)",
            (f"Продукт {i}", f"описание {i}", i * 100)
        )
    connection.commit()
    connection.close()


def is_correct_email(email):
    return bool(re.fullmatch(r'([\x00-\x7F]+)@([\x00-\x7F]+)\.([\x00-\x7F]{2,4})\Z', email))


if __name__ == '__main__':
    pass
