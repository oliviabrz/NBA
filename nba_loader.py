#!/usr/bin/env python3

import json
from flask import Flask, request, jsonify
import requests
import pyodbc 
from nba_db_record import TeamRecord 


app = Flask(__name__)

@app.route('/api/nba/load/teams', methods=['GET'])
def load_teams():
    url = 'https://www.balldontlie.io/api/v1/teams'
    json_dict = call_api(url)
    #print(res)
    cn = SqlConnection()

    team_rec_list = extract_teams_from_json(json_dict)
    for team_rec in team_rec_list:
        team_rec.insert(cn)
    # cursor.execute("SELECT @@version;")
    # row = cursor.fetchone()
    # while row:
    #     print(row)
    #     row = cursor.fetchone()
    return 'it worked!'

def extract_teams_from_json(json_dict):
    rec_list = []
    id_counter = 1
    for items in json_dict['data']:   
        #create new instance of class TeamRecord 
        teamrec = TeamRecord()
    
        #populate TeamRecord with values from the json_dict items 
        teamrec.ID = id_counter
        teamrec.Abbreviation = items['abbreviation'] 
        teamrec.City = items['city']
        teamrec.Conference = items['conference']
        teamrec.Division = items['division'] 
        teamrec.FullName = items['full_name']
        teamrec.Name = items['name']

        #increase id_counter by 1 
        id_counter += 1

        #add teamrec instance to rec_list 
        rec_list.append(teamrec)
        
    return rec_list


def call_api(url):    
    response = requests.get(url)

    if response.ok:
        json_dict = json.loads(response.text)
        #print(response.text)
        return json_dict
    else:
        msg = f'NBA api error - status_code = {response.status_code}, text = {response.text}'
        #print(msg)
        return {'error': msg}

class SqlConnection:
    def __init__(self):
        # here we are telling python what to connect to (our SQL Server)
        driver = "Driver={ODBC Driver 17 for SQL Server};"
        cnstring = f'{driver}Server=hello-world.database.windows.net;Database=NBA;UID=olivia;PWD=LearnSql123;' 

        #connect to server
        self.cnxn = pyodbc.connect(cnstring)

    #return connection variable
    def connection(self):
        return self.cnxn

    #return cursor from connection
    def cursor(self):
        return self.cnxn.cursor() 

        # initialise query attribute
        #self.query = "-- {}\n\n-- Made in Python".format(datetime.now()


if __name__ == '__main__':
    app.run()