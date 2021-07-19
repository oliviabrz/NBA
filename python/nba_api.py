#!/usr/bin/env python3

import json
from nba_db_record import PlayerGameStatsRecord, PlayerRecord, TeamRecord, GameRecord
from flask import Flask, request, jsonify
import requests
import pyodbc
from json import JSONEncoder
from sql_connection import SqlConnection


app = Flask(__name__)

# ------------------------
# Player Api's
# ------------------------


@app.route('/api/nba/player', methods=['GET'])
def get_player_by_name():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    player_rec = PlayerRecord()
    player_rec.FirstName = first_name
    player_rec.LastName = last_name

    cn = SqlConnection()

    player_rec.get_player_rec_by_name(cn)
    json_rec = player_rec.__dict__
    response = jsonify(json_rec)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route('/api/nba/player/list', methods=['GET'])
def get_player_list():

    player_rec = PlayerRecord()

    cn = SqlConnection()

    player_list = player_rec.get_player_list(cn)

    # iterate over each player rec and convert into dictionary
    player_json_list = []
    for rec in player_list:
        player_json_list.append(rec.__dict__)

    response = jsonify(player_json_list)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

# ------------------------
# Team Api's
# ------------------------


@app.route('/api/nba/team', methods=['GET'])
def get_team_by_abbreviation():
    # get query string parameter from the Flask request object
    abbreviation = request.args.get('abbreviation')

    # create team record instance
    team_rec = TeamRecord()

    # assign the abbreviation field with the value of the query string parameter
    team_rec.Abbreviation = abbreviation

    # get sql connection
    cn = SqlConnection()

    # populate record instance with database values
    team_rec.get_team_rec_by_abbreviation(cn)

    # convert record instance to a dictionary
    json_rec = team_rec.__dict__

    # create a Flask response object and set the mime-type to application/json
    response = jsonify(json_rec)

    # allow CORS (Cross Origin Resource Sharing)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route('/api/nba/team/list', methods=['GET'])
def get_team_list():

    team_rec = TeamRecord()

    cn = SqlConnection()

    # get list of TeamRecord instances
    team_list = team_rec.get_team_list(cn)

    # list to hold TeamRecord dictionaries
    team_json_list = []

    # iterate over each TeamRecord instance, convert it to a dictionary and
    # add to dictionary list
    for rec in team_list:
        team_json_list.append(rec.__dict__)

    response = jsonify(team_json_list)

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

# ------------------------
# Game Api's
# ------------------------


@app.route('/api/nba/game/list', methods=['GET'])
def get_game_list():
    game_rec = GameRecord()

    cn = SqlConnection()

    # get list of TeamRecord instances
    game_list = game_rec.get_game_list(cn)

    # list to hold TeamRecord dictionaries
    game_json_list = []

    # iterate over each TeamRecord instance, convert it to a dictionary and
    # add to dictionary list
    for rec in game_list:
        game_json_list.append(rec.__dict__)

    response = jsonify(game_json_list)

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

# ------------------------
# Game Stats Api
# ------------------------


@app.route('/api/nba/game/stats/list', methods=['GET'])
def get_game_stats_list():
    response = {}

    # get query string parameter from the Flask request object
    season = request.args.get('season')
    if season is None:
        season = 2020

    stat = request.args.get('stat')
    if stat is None:
        return response

    game_stats_rec = PlayerGameStatsRecord()

    cn = SqlConnection()

    # get list of TeamRecord instances
    game_stats_list = game_stats_rec.get_game_stats_list(cn, season, stat)

    # list to hold TeamRecord dictionaries
    game_stats_json_list = []

    # iterate over each TeamRecord instance, convert it to a dictionary and
    # add to dictionary list
    for rec in game_stats_list:
        if stat == 'Min':
            game_stats_json_list.append({'Min': rec.Min})
        elif stat == 'Ast':
            game_stats_json_list.append({'Ast': rec.Ast})
        elif stat == 'Blk':
            game_stats_json_list.append({'Blk': rec.Blk})
        elif stat == 'Dreb':
            game_stats_json_list.append({'Dreb': rec.Dreb})
        elif stat == 'Fg3a':
            game_stats_json_list.append({'Fg3a': rec.Fg3a})
        elif stat == 'Fg3m':
            game_stats_json_list.append({'Fg3m': rec.Fg3m})
        elif stat == 'Fg3Pct':
            game_stats_json_list.append({'Fg3Pct': rec.Fg3Pct})
        elif stat == 'Fga':
            game_stats_json_list.append({'Fga': rec.Fga})
        elif stat == 'Fgm':
            game_stats_json_list.append({'Fgm': rec.Fgm})
        elif stat == 'FgPct':
            game_stats_json_list.append({'FgPct': rec.FgPct})
        elif stat == 'Fta':
            game_stats_json_list.append({'Fta': rec.Fta})
        elif stat == 'Ftm':
            game_stats_json_list.append({'Ftm': rec.Ftm})
        elif stat == 'FtPct':
            game_stats_json_list.append({'FtPct': rec.FtPct})
        elif stat == 'Oreb':
            game_stats_json_list.append({'Oreb': rec.Oreb})
        elif stat == 'Pf':
            game_stats_json_list.append({'Pf': rec.Pf})
        elif stat == 'Pts':
            game_stats_json_list.append({'Pts': rec.Pts})
        elif stat == 'Reb':
            game_stats_json_list.append({'Reb': rec.Reb})
        elif stat == 'Stl':
            game_stats_json_list.append({'Stl': rec.Stl})
        elif stat == 'Turnover':
            game_stats_json_list.append({'Turnover': rec.Turnover})
        # game_stats_json_list.append(rec.__dict__)

    response = jsonify(game_stats_json_list)

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == '__main__':
    app.run(port=5000)
