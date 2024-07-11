import sqlite3
import pandas as pd
# from utils.sql_command import *

from .sql_command import *
'''
Database:

venv_info(id, project_path, venv_name, created_date, requirement_file, connect_status)

'''

def check_database(con):
    cur = con.cursor()
    cur.execute(create_venv_info_sql)

def connect_check_database(database_path: str):
    con = sqlite3.connect(database_path)
    check_database(con)
    return con


def insert_data(con: sqlite3.Connection, *args, **kwargs):
    cur = con.cursor()
    cur.execute(insert_into_venv_info_sql, (kwargs['project_path'], kwargs['venv_name'], kwargs['created_date'], kwargs['requirement_file'], kwargs['connect_status']))
    con.commit()

def update_data(con: sqlite3.Connection, *args, **kwargs):
    cur = con.cursor()
    cur.execute(update_connect_status_venv_info_sql, (kwargs['connect_status'], kwargs['venv_name']))
