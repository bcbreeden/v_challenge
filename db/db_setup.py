import sqlite3

def create_subj_info_table():
    conn = sqlite3.connect('db/veeva.db')
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS subject_information (
        subj_id TEXT PRIMARY KEY,
        site_number TEXT,
        dob DATE,
        sex TEXT,
        rand_id TEXT,
        prev_treatment TEXT,
        severity TEXT,
        cohort TEXT,
        status TEXT,
        status_date DATE,
        next_event TEXT
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def create_credentials_table():
    conn = sqlite3.connect('db/veeva.db')
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS credentials (
        login TEXT PRIMARY KEY,
        pw TEXT,
        login_url TEXT
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()