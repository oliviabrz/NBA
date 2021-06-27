#!/usr/bin/env python3

import json
from flask import Flask, request, jsonify
import requests
import pyodbc 
from nba_db_record import TeamRecord, PlayerRecord, PlayerGameStatsRecord
from nba_extractor import extract_teams_from_json, extract_players_from_json, extract_player_game_stats_from_json

app = Flask(__name__)

@app.route('/api/nba/load/teams', methods=['GET'])
def load_teams():
    url = 'https://www.balldontlie.io/api/v1/teams'
    json_dict = call_api(url)
    
    cn = SqlConnection()

    team_rec_list = extract_teams_from_json(json_dict)
    for team_rec in team_rec_list:
        team_rec.insert(cn)
        #print(team_rec)
    return 'it worked!'

#----------
@app.route('/api/nba/load/players', methods=['GET'])
def load_players():
    url = 'https://www.balldontlie.io/api/v1/players?per_page=100&page='

    cn = SqlConnection()

    for page_number in range(1,36):
        #create new url including page number query string parameter
        new_url = url + str(page_number)

        #call api passing in new_url and receive a json dictionary of player data
        json_dict = call_api(new_url)

        #call method passing in json dict and receive an array of PlayerRecord instances
        player_rec_list = extract_players_from_json(json_dict)

        #iterate over array of PlayerRecord instances and insert into database 
        for player_rec in player_rec_list:
            #get team ID from database using TeamAbbreviation 
            #player_rec.get_team_id(cn, player_rec.TeamAbbreviation)
            
            #insert into database 
            player_rec.insert(cn)

    return 'it worked!'

#----------
@app.route('/api/nba/load/game/player/stats', methods=['GET'])
def load_player_game_stats():  
    url = 'https://www.balldontlie.io/api/v1/stats?start_date=2018-01-01&per_page=100&page='

    cn = SqlConnection()

    for page_number in range(1,3):
        new_url = url + str(page_number)
        json_dict = call_api(new_url)
        
        #extract game and player lists
        records_lists = extract_player_game_stats_from_json(json_dict)

        #get access to each list
        game_rec_list = records_lists[0]
        player_rec_list = records_lists[1]

        #iterate over game list and insert record s
        for game_rec in game_rec_list:
            game_rec.insert(cn)
        
        #iterate over player list and insert record 
        for player_rec in player_rec_list:
            player_rec.insert(cn)

    return 'it worked!'

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

    #----------
    #return connection variable
    def connection(self):
        return self.cnxn

    #----------
    #return cursor from connection
    def cursor(self):
        return self.cnxn.cursor() 

#----------
if __name__ == '__main__':
    app.run()