from db import db_setup, db_credentials
'''
Setup script to be run before the test is executed. This creates and populates the databases required for the test to function.
'''
if __name__ == '__main__':
    db_setup.create_subj_info_table()
    db_setup.create_credentials_table()
    db_credentials.create_credentials()