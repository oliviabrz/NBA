#!/usr/bin/env python3

import pyodbc 
import json
import datetime

def rnull(val, cmp):
    return val if val != cmp else 'NULL'

class TeamRecord:
    def __init__(self):
        self.ID = None
        self.Abbreviation = None
        self.City = None
        self.Conference = None
        self.Division = None
        self.FullName = None
        self.Name = None 

#----------
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.Team
        (ID, Abbreviation, City, Conference, Division, FullName, Name)
        values ({self.ID}, '{self.Abbreviation}', '{self.City}', '{self.Conference}', '{self.Division}', 
        '{self.FullName}', '{self.Name}')
        """
        #print(insert_statement)
        #execute insert statement from the cursor
        cn.cursor().execute(insert_statement)
        
        #commit insert statement to database from the connection
        cn.connection().commit()

    def get_team_rec_by_abbreviation(self, cn):
        select_statement = f"""
        select ID, Abbreviation, City, Conference, Division, FullName, Name
        from NBA.Team t
        where t.Abbreviation = '{self.Abbreviation}'
        """
        #print(select_statement)

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        row = cursor.fetchone()

        #assign the instance attributes with the values from the row
        self.ID = row.ID
        self.Abbreviation = row.Abbreviation
        self.City = row.City
        self.Conference = row.Conference
        self.Division = row.Division
        self.FullName = row.FullName
        self.Name = row.Name

    def get_team_list(self, cn):
        team_list = []
        select_statement = f"""
        select ID, Abbreviation, City, Conference, Division, FullName, Name
        from NBA.Team t
        """
        #print(select_statement)

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        for row in cursor.fetchall():
            rec = TeamRecord()
        
            rec.ID = row.ID
            rec.Abbreviation = row.Abbreviation
            rec.City = row.City
            rec.Conference = row.Conference
            rec.Division = row.Division
            rec.FullName = row.FullName
            rec.Name = row.Name

            team_list.append(rec)
        
        return team_list

#----------
    def __str__(self):
        string = f"""ID: {self.ID}, Abbreviation: {self.Abbreviation}, City: {self.City}, 
        Conference: {self.Conference}, Division: {self.Division}, FullName: {self.FullName},
        Name: {self.Name}\n"""
        return string
        
#----------
    def __repr__(self):
        string = f"""ID: {self.ID}, Abbreviation: {self.Abbreviation}, City: {self.City}, 
        Conference: {self.Conference}, Division: {self.Division}, FullName: {self.FullName},
        Name: {self.Name}\n"""         
        return string

class PlayerRecord:
    def __init__(self):
        self.ID = None
        self.FirstName = None
        self.LastName = None
        self.Position = None
        self.HeightFeet = None
        self.HeightInches = None
        self.WeightPounds = None
        self.TeamID = None
        #self.TeamAbbreviation = None

#----------
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.Player
        (ID, FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID)
        values ({self.ID}, '{self.FirstName}', '{self.LastName}', 
        '{rnull(self.Position, '')}',
        {rnull(self.HeightFeet, None)},
        {rnull(self.HeightInches, None)},
        {rnull(self.WeightPounds, None)}, 
        {self.TeamID})
        """
        
        cursor = cn.cursor()
        cursor.execute(insert_statement)
    
        #commit insert statement to database from the connection
        cn.connection().commit()

#----------
    def get_player_rec_by_name(self, cn):
        select_statement = f"""
        select ID, FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID
        from NBA.Player p
        where p.FirstName = '{self.FirstName}' and p.LastName = '{self.LastName}'
        """
        #print(select_statement)

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        row = cursor.fetchone()

        #print(str(row.FirstName))
        #print(ascii(row.FirstName))
        
        self.ID = row.ID
        self.FirstName = row.FirstName
        self.LastName = row.LastName
        self.Position = row.Position
        self.HeightFeet = row.HeightFeet
        self.HeightInches = row.HeightInches
        self.WeightPounds = row.WeightPounds
        self.TeamID = row.TeamID

    def get_player_list(self, cn):
        player_list = []
        select_statement = f"""
        select ID, FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID
        from NBA.Player p
        """
        #print(select_statement)

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        for row in cursor.fetchall():
            rec = PlayerRecord()
        
            rec.ID = row.ID
            rec.FirstName = row.FirstName
            rec.LastName = row.LastName
            rec.Position = row.Position
            rec.HeightFeet = row.HeightFeet
            rec.HeightInches = row.HeightInches
            rec.WeightPounds = row.WeightPounds
            rec.TeamID = row.TeamID

            player_list.append(rec)
        
        return player_list

#----------
    # def get_team_id(self, cn, team_abbreviation):
    #     select_statement = f"""
    #      select ID from NBA.Team where Abbreviation = '{team_abbreviation}'
    #      """

    #      cursor = cn.cursor()
    #      cursor.execute(select_statement)
        
    #      result = cursor.fetchone()
        
    #      if result != None:
    #          self.TeamID = result[None]
    #      else:
    #          print (f'error retrieving ID for Abbreviation [{team_abbreviation}]')

#----------
    def __str__(self):
        string = f"""ID: {self.ID}, FirstName: {self.FirstName}, LastName: {self.LastName}, 
        Position: {self.Position}, HeightFeet: {self.HeightFeet}, HeightInches: {self.HeightInches},
        WeightPounds: {self.WeightPounds}, TeamID: {self.TeamID}\n"""
        return string

#----------
    def __repr__(self):
        string = f"""ID: {self.ID}, FirstName: {self.FirstName}, LastName: {self.LastName}, 
        Position: {self.Position}, HeightFeet: {self.HeightFeet}, HeightInches: {self.HeightInches},
        WeightPounds: {self.WeightPounds}, TeamID: {self.TeamID}\n"""
        return string

class PlayerGameStatsRecord:
    def __init__(self):
        self.GameID = None
        self.PlayerID = None
        self.TeamID = None
        
        self.Ast = None
        self.Blk = None
        self.Dreb = None
        self.Fg3Pct = None
        self.Fg3a = None
        self.Fg3m = None
        self.FgPct = None
        self.Fga = None
        self.Fgm = None
        self.FtPct = None
        self.Fta = None
        self.Ftm = None
        self.Min = None
        self.Oreb = None
        self.Pf = None
        self.Pts = None
        self.Reb = None
        self.Stl = None
        self.Turnover = None

        self.GameDate = None
        self.PostSeason = None

#----------
    def build_sql_values(self):
        sql = f"""{rnull(self.Ast, None)}, {rnull(self.Blk, None)}, {rnull(self.Dreb, None)},
        {rnull(self.Fg3Pct, None)}, {rnull(self.Fg3a, None)}, {rnull(self.Fg3m, None)},
        {rnull(self.FgPct, None)}, {rnull(self.Fga, None)}, {rnull(self.Fgm, None)}, {rnull(self.FtPct, None)}, 
        {rnull(self.Fta, None)}, {rnull(self.Ftm, None)}, {rnull(self.GameID, None)}, 
        {rnull(self.Oreb, None)}, {rnull(self.Pf, None)}, {rnull(self.PlayerID, None)}, 
        {rnull(self.Pts, None)}, {rnull(self.Reb, None)}, {rnull(self.Stl, None)}, {rnull(self.Turnover, None)}, """

        if self.Min is not None:
            sql += f"'{self.Min}'"
        else:
            sql += 'NULL'

        return sql

#----------
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.PlayerGameStats
        (Ast, Blk, Dreb, Fg3Pct, Fg3a, Fg3m, FgPct, Fga, Fgm, FtPct, Fta, Ftm, GameID, 
        Oreb, Pf, PlayerID, Pts, Reb, Stl, Turnover, Min)
        values ({self.build_sql_values()})"""

        # values ({rnull(self.Ast, None)}, {rnull(self.Blk, None)}, {rnull(self.Dreb, None)},
        # {rnull(self.Fg3Pct, None)}, {rnull(self.Fg3a, None)}, {rnull(self.Fg3m, None)},
        # {rnull(self.FgPct, None)}, {rnull(self.Fga, None)}, {rnull(self.Fgm, None)}, {rnull(self.FtPct, None)}, 
        # {rnull(self.Fta, None)}, {rnull(self.Ftm, None)}, {rnull(self.GameID, None)}, 
        # '{rnull(self.Min, None)}',
        # {rnull(self.Oreb, None)}, {rnull(self.Pf, None)}, {rnull(self.PlayerID, None)}, 
        # {rnull(self.Pts, None)}, {rnull(self.Reb, None)}, {rnull(self.Stl, None)}, {rnull(self.Turnover, None)})
        # """
        #print(insert_statement)

        cn.cursor().execute(insert_statement)
        cn.connection().commit()
    
    def get_game_stats_list(self, cn, season, stat):
        game_stats_list = []
        select_statement = f"""
        SELECT {stat}, GameDate, PostSeason
        FROM NBA.PlayerGameStats pgs 
        join NBA.Game g 
	        on pgs.GameID = g.ID 
        where g.Season >= {season}
        order by GameDate ASC
        """
        #print(select_statement)

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        for row in cursor.fetchall():
            rec = PlayerGameStatsRecord()

            self.GameDate = rec.GameDate
            rec.GameDate= row.GameDate.strftime('%Y-%m-%d')
            self.PostSeason = rec.PostSeason
            rec.PostSeason = bool(row.PostSeason)

            if stat == 'Min':
                rec.Min= str(row.Min)
            elif stat == 'Ast':
                rec.Ast= str(row.Ast)
            elif stat == 'Blk':
                rec.Blk = str(row.Blk)
            elif stat == 'Dreb':
                rec.Dreb = str(row.Dreb)
            elif stat == 'Fg3a':
                rec.Fg3a = str(row.Fg3a)
            elif stat == 'Fg3m':
                rec.Fg3m = str(row.Fg3m)
            elif stat == 'Fg3Pct':
                rec.Fg3Pct= str(row.Fg3Pct)
            elif stat == 'Fga':
                rec.Fga= str(row.Fga)
            elif stat == 'Fgm':
                rec.Fgm= str(row.Fgm)
            elif stat == 'FgPct':
                rec.FgPct = str(row.FgPct)
            elif stat == 'Fta':
                rec.Fta= str(row.Fta)
            elif stat == 'Ftm':
                rec.Ftm = str(row.Ftm)
            elif stat == 'FtPct':
                rec.FtPct = str(row.FtPct)
            elif stat == 'Oreb':
                rec.Oreb = str(row.Oreb)
            elif stat == 'Pf':
                rec.Pf = str(row.Pf)
            elif stat == 'Pts':
                rec.Pts = str(row.Pts)
            elif stat == 'Reb':
                rec.Reb = str(row.Reb)
            elif stat == 'Stl':
                rec.Stl = str(row.Stl)
            elif stat == 'Turnover':
                rec.Turnover = str(row.Turnover)
            
            game_stats_list.append(rec)
        
        return game_stats_list

#----------
    def __str__(self):
        string = f"""Ast: {self.Ast}, Blk: {self.Blk}, Dreb: {self.Dreb}, Fg3Pct: {self.Fg3Pct},
        Fg3a: {self.Fg3a}, Fg3m: {self.Fg3m}, FgPct: {self.FgPct}, Fga: {self.Fga}, Fgm: {self.Fgm}, 
        FtPct: {self.FtPct}, Fta: {self.Fta}, Ftm: {self.Ftm}, GameID: '{self.GameID}', Min: {self.Min}, 
        Oreb: {self.Oreb}, Pf: {self.Pf}, PlayerID: '{self.PlayerID}', Pts: {self.Pts}, Reb: {self.Reb}, 
        Stl: {self.Stl}, TeamID: '{self.TeamID}', Turnover: {self.Turnover}\n"""
        return string
        
#----------
    def __repr__(self):
        string = f"""Ast: {self.Ast}, Blk: {self.Blk}, Dreb: {self.Dreb}, Fg3Pct: {self.Fg3Pct},
        Fg3a: {self.Fg3a}, Fg3m: {self.Fg3m}, FgPct: {self.FgPct}, Fga: {self.Fga}, Fgm: {self.Fgm}, 
        FtPct: {self.FtPct}, Fta: {self.Fta}, Ftm: {self.Ftm}, GameID: '{self.GameID}', Min: {self.Min}, 
        Oreb: {self.Oreb}, Pf: {self.Pf}, PlayerID: '{self.PlayerID}', Pts: {self.Pts}, Reb: {self.Reb}, 
        Stl: {self.Stl}, TeamID: '{self.TeamID}', Turnover: {self.Turnover}\n"""
        return string

class GameRecord:
    def __init__(self):
        self.ID = None
        self.GameDate = None
        self.HomeTeamID = None
        self.HomeTeamScore = None
        self.Period = None
        self.PostSeason = None
        self.Season = None
        self.Status = None
        self.GameTime = None
        self.VisitorTeamID = None
        self.VisitorTeamScore = None
        self.HomeTeamAbbr = None
        self.HomeTeamFullName = None
        self.VisitorTeamAbbr = None
        self.VisitorTeamFullName = None

#----------  
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.Game
        (ID, GameDate, HomeTeamID, HomeTeamScore, Period, PostSeason, Season, Status, 
        GameTime, VisitorTeamID, VisitorTeamScore)
        values ({rnull(self.ID, None)}, '{rnull(self.GameDate, None)}', {rnull(self.HomeTeamID, None)},
        {rnull(self.HomeTeamScore, None)}, {rnull(self.Period, None)}, {rnull(self.PostSeason, None)},
        {rnull(self.Season, None)}, '{rnull(self.Status, None)}', '{rnull(self.GameTime, None)}', 
        {rnull(self.VisitorTeamID, None)}, {rnull(self.VisitorTeamScore, None)})
        """
        try:            
            cn.cursor().execute(insert_statement)
            cn.connection().commit()
        except Exception as e:
            print (f"An exception occurred [{e}]")

    def get_game_list(self, cn):
        game_list = []
        select_statement = f"""
        select g.ID, GameDate, HomeTeamID, ht.Abbreviation as HomeTeamAbbr,
        ht.FullName as HomeTeamFullName, HomeTeamScore, VisitorTeamID,
        vt.Abbreviation as VisitorTeamAbbr, vt.FullName as VisitorTeamFullName,
        VisitorTeamScore, Period, PostSeason, Season, Status, GameTime	   
        from Game g 
        join Team ht 
	        on g.HomeTeamID = ht.ID 
        join Team vt
	        on g.VisitorTeamID = vt.ID
        order by g.ID
        """
        #print(select_statement)

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        for row in cursor.fetchall():
            rec = GameRecord()
        
            rec.ID = row.ID
            rec.GameDate= row.GameDate.strftime('%Y-%m-%d')
            rec.HomeTeamID = row.HomeTeamID
            rec.HomeTeamScore = row.HomeTeamScore
            rec.Period = row.Period
            rec.PostSeason = row.PostSeason
            rec.Season = row.Season
            rec.Status = row.Status
            rec.GameTime = row.GameTime
            rec.VisitorTeamID = row.VisitorTeamID
            rec.VisitorTeamScore = row.VisitorTeamScore
            rec.HomeTeamAbbr = row.HomeTeamAbbr
            rec.HomeTeamFullName = row.HomeTeamFullName
            rec.VisitorTeamAbbr = row.VisitorTeamAbbr
            rec.VisitorTeamFullName = row.VisitorTeamFullName
            
            game_list.append(rec)
        
        return game_list

#---------- 
    def __str__(self):
        string = f"""ID: {self.ID}, Date: {self.Date}, HomeTeamID: {self.HomeTeamID}, 
        HomeTeamScore: {self.HomeTeamScore}, Period: {self.Period}, PostSeason: {self.PostSeason},
        Season: {self.Season}, Status: {self.Status}, Time: {self.Time}, VisitorTeamID: {self.VisitorTeamID}, 
        VisitorTeamScore: {self.VisitorTeamScore}\n"""
        return string

#----------
    def __repr__(self):
        string = f"""ID: {self.ID}, Date: {self.Date}, HomeTeamID: {self.HomeTeamID}, 
        HomeTeamScore: {self.HomeTeamScore}, Period: {self.Period}, PostSeason: {self.PostSeason},
        Season: {self.Season}, Status: {self.Status}, Time: {self.Time}, VisitorTeamID: {self.VisitorTeamID}, 
        VisitorTeamScore: {self.VisitorTeamScore}\n"""
        return string

class StatAggregateRecord:
    def __init__(self):
        self.StatName = None
        self.StatDate = None
        self.StatAvg = None
        self.StatMax = None
    
    def get_stat_aggregate(self,cn, season, stat):
        stat_aggregate_list = []
        select_statement = f"""
        SELECT DATE_FORMAT(GameDate, '%m-%Y') as StatDate, AVG({stat}) as StatAvg, Max({stat}) as StatMax
        FROM  NBA.PlayerGameStats pgs 
        join NBA.Game g 
	        on pgs.GameID = g.ID 
        where g.Season >= {season}
        GROUP BY DATE_FORMAT(GameDate, '%m-%Y')"""

        cursor = cn.cursor()
        cursor.execute(select_statement)

        for row in cursor.fetchall():
            rec = StatAggregateRecord()
        
            rec.StatName= stat
            rec.StatDate = row.StatDate
            rec.StatAvg = str(row.StatAvg)
            rec.StatMax = str(row.StatMax)
            
            stat_aggregate_list.append(rec)
        
        return stat_aggregate_list

    def __str__(self):
        string = f"""StatName: {self.StatName}, StatDate: {self.StatDate}, StatAvg: {self.StatAvg}, 
        StatMax: {self.StatMax}\n"""
        return string

    def __repr__(self):
        string = f"""StatName: {self.StatName}, StatDate: {self.StatDate}, StatAvg: {self.StatAvg}, 
        StatMax: {self.StatMax}\n"""
        return string