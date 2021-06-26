#!/usr/bin/env python3

from nba_db_record import GameRecord, TeamRecord, PlayerRecord, PlayerGameStatsRecord
import re

def extract_teams_from_json(json_dict):
    rec_list = []

    for items in json_dict['data']:   
        #create new instance of class TeamRecord 
        teamrec = TeamRecord()
    
        #populate TeamRecord with values from the json_dict items 
        teamrec.ID = items['id']
        teamrec.Abbreviation = items['abbreviation'] 
        teamrec.City = items['city']
        teamrec.Conference = items['conference']
        teamrec.Division = items['division'] 
        teamrec.FullName = items['full_name']
        teamrec.Name = items['name']

        #add teamrec instance to rec_list 
        rec_list.append(teamrec)
        
    return rec_list

#----------
def extract_players_from_json(json_dict):
    rec_list = []

    for items in json_dict['data']:   
        #create new instance of class PlayerRecord 
        player_rec = PlayerRecord()

        #get Team Abbreviation 
        #team = items['team']
        #player_rec.TeamAbbreviation = team['abbreviation']      
    
        #populate record with values from the json_dict items 
        player_rec.ID = items['id']
        player_rec.FirstName = items['first_name'].replace("'", "")
        player_rec.LastName = items['last_name'].replace("'", "")
        player_rec.Position = items['position']
        player_rec.HeightFeet = items['height_feet'] 
        player_rec.HeightInches = items['height_inches']
        player_rec.WeightPounds = items['weight_pounds']
        team = items['team']
        player_rec.TeamID = team['id']
        
        #add rec instance to rec list 
        rec_list.append(player_rec)
        
    return rec_list

#----------
def extract_player_game_stats_from_json(json_dict):
    rec_list = []
    game_id_dict = {}

    for items in json_dict['data']:
        player_stats_rec = PlayerGameStatsRecord()

        #get json game object
        game = items['game']
        game_id = game['id']



        #exract player stats
        player_stats_rec.GameID = game_id
        player_stats_rec.Ast = items['ast']
        player_stats_rec.Blk = items['blk']
        player_stats_rec.Dreb = items['dreb']
        player_stats_rec.Fg3Pct = items['fg3_pct']
        player_stats_rec.Fg3a = items['fg3a']
        player_stats_rec.Fg3m = items['fg3m']
        player_stats_rec.FgPct = items['fg_pct']
        player_stats_rec.Fga = items['fga']
        player_stats_rec.Fgm = items['fgm']
        player_stats_rec.FtPct = items['ft_pct']
        player_stats_rec.Fta = items['fta']
        player_stats_rec.Ftm = items['ftm']
        player_stats_rec.Min = items['min']
        player_stats_rec.Oreb = items['oreb']
        player_stats_rec.Pf = items['pf']
        player_stats_rec.Pts = items['pts']
        player_stats_rec.Reb = items['reb']
        player_stats_rec.Stl = items['stl']
        player_stats_rec.Turnover = items['turnover']

        #extract game info
        game_rec = GameRecord()
        
        game_rec.ID = game_id
        match = re.match(r'([0-9]{4}-[0-9]{2}-[0-9]{2})', game['date'])
        if match != None:
            game_rec.GameDate = match.group(0)
        game_rec.HomeTeamID = game['home_team_id']
        game_rec.HomeTeamScore = game['home_team_score']
        game_rec.Period = game['period']
        game_rec.PostSeason = game['postseason']
        game_rec.Season = game['season']
        game_rec.Status = game['status']
        #game_rec.GameTime = game['time']
        game_rec.VisitorTeamID = game['visitor_team_id']
        game_rec.VisitorTeamScore = game['visitor_team_score']

        #extract IDs
        player = items['player']
        player_stats_rec.PlayerID = player['id']
        team = items['team']
        player_stats_rec.TeamID = team['id']

        rec_list.append((game_rec, player_stats_rec))

    return rec_list

