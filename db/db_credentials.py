import sqlite3
from . import constants

def create_credentials():
    conn = sqlite3.connect('db/veeva.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT OR REPLACE INTO credentials (
        login, pw, login_url
    ) VALUES (?, ?, ?);
    '''

    cursor.execute(insert_query, (
        constants.LOGIN,
        constants.PW,
        constants.LOGIN_URL
    ))

    conn.commit()
    conn.close()

def fetch_credentials():
    conn = sqlite3.connect('db/veeva.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    fetch_query = "SELECT * FROM credentials;"
    cursor.execute(fetch_query)

    row = cursor.fetchone()

    conn.close()
    return row