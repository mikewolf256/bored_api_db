import json
import requests
from pandas.io.json import json_normalize
import pandas as pd



import sqlite3

def create_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS actvities
            ([activity] TEXT, [type] TEXT,
            [participants] FLOAT, [price] FLOAT, [link] VARCHAR,
            [key] INTEGER, [accessibility] FLOAT
            )
            ''')
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)

def insert_data(db_name):
    url = "https://www.boredapi.com/api/activity"
    #params = {'type':'fun'}
    try:
        response = requests.get(url,verify=False)
        things = json.loads(response.text)
        if response.status_code == 200:
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            c.execute('INSERT INTO actvities VALUES (?,?,?,?,?,?,?)', [
                things['activity'],
                things['type'],
                things['participants'],
                things['price'],
                things['link'],
                things['key'],
                things['accessibility'],
                ])
            conn.commit()
            conn.close()
        else:
            print(f"The error is {response.status_code}")
    except Exception as e:
        print(e)

create_db("NameAPI.db")
insert_data("NameAPI.db")


