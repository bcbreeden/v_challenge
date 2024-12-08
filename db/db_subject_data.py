import sqlite3

def insert_subject_data(data):
    '''Insert a dictionary of subject data into the subject_information table.'''
    conn = sqlite3.connect('db/veeva.db')
    cursor = conn.cursor()

    insert_query = """
    INSERT OR REPLACE INTO subject_information (
        site_number, subj_id, dob, sex, rand_id, prev_treatment, severity, cohort, status, status_date, next_event
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    cursor.execute(insert_query, (
        data['site_number'],
        data['subj_id'],
        data['dob'],
        data['sex'],
        data['rand_id'],
        data['prev_treatment'],
        data['severity'],
        data['cohort'],
        data['status'],
        data['status_date'],
        data['next_event']
    ))

    conn.commit()
    conn.close()

def fetch_all_subjects():
    '''Fetch all rows from the subject_information table and return them.'''
    conn = sqlite3.connect('db/veeva.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    fetch_query = "SELECT * FROM subject_information;"
    cursor.execute(fetch_query)

    rows = cursor.fetchall()

    conn.close()
    return rows