#!/usr/bin/env python3

import json
from flask import Flask, request, jsonify
import requests
import pyodbc 
from nba_db_record import TeamRecord, PlayerRecord


app = Flask(__name__)

#----------
@app.route('/api/nba/load/teams', methods=['GET'])
def load_teams():
    url = 'https://www.balldontlie.io/api/v1/teams'
    json_dict = call_api(url)
    #print(res)
    cn = SqlConnection()

    team_rec_list = extract_teams_from_json(json_dict)
    for team_rec in team_rec_list:
        team_rec.insert(cn)
        #print(team_rec)
    return 'it worked!'

#----------
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

#----------
@app.route('/api/nba/load/players', methods=['GET'])
def load_players():
    url = 'https://www.balldontlie.io/api/v1/players'
    json_dict = call_api(url)
    #print(res)
    cn = SqlConnection()

    player_rec_list = extract_players_from_json(json_dict)
    for player_rec in player_rec_list:
        player_rec.get_team_id(cn, player_rec.TeamAbbreviation)
        player_rec.insert(cn)
    return 'it worked!'

#----------
def extract_players_from_json(json_dict):
    rec_list = []
    id_counter = 1
    for items in json_dict['data']:   
        #create new instance of class PlayerRecord 
        player_rec = PlayerRecord()

        #get Team Abbreviation 
        team = items['team']
        player_rec.TeamAbbreviation = team['abbreviation']        
    
        #populate record with values from the json_dict items 
        player_rec.ID = id_counter
        player_rec.FirstName = items['first_name'] 
        player_rec.LastName = items['last_name']
        player_rec.Position = items['position']
        player_rec.HeightFeet = items['height_feet'] 
        player_rec.HeightInches = items['height_inches']
        player_rec.WeightPounds = items['weight_pounds']

        #increase id_counter by 1 
        id_counter += 1

        #add rec instance to rec list 
        rec_list.append(player_rec)
        
    return rec_list

#----------
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

#----------
class SqlConnection:
    def __init__(self):
        # here we are telling python what to connect to (our SQL Server)
        driver = "Driver={MySQL ODBC 8.0 ANSI Driver};"
        cnstring = f'{driver}Server=localhost;Database=NBA;UID=root;PWD=LearnSql123;' 

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

#----------
if __name__ == '__main__':
    app.run()