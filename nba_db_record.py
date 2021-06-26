#!/usr/bin/env python3

import pyodbc 

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
        values ({self.ID}, '{self.Abbreviation}', '{self.City}', '{self.Conference}', '{self.Division} '{self.FullName}', '{self.Name}')
        """
        #print(insert_statement)
        #execute insert statement from the cursor
        cn.cursor().execute(insert_statement)
        
        #commit insert statement to database from the connection
        cn.connection().commit()

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
    # def get_team_id(self, cn, team_abbreviation):
    #     select_statement = f"""
    #     select ID from NBA.Team where Abbreviation = '{team_abbreviation}'
    #     """

    #     cursor = cn.cursor()
    #     cursor.execute(select_statement)
        
    #     result = cursor.fetchone()
        
    #     if result != None:
    #         self.TeamID = result[None]
    #     else:
    #         print (f'error retrieving ID for Abbreviation [{team_abbreviation}]')

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

#----------
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.PlayerGameStats
        (Ast, Blk, Dreb, Fg3Pct, Fg3a, Fg3m, FgPct, Fga, Fgm, FtPct, Fta, Ftm, GameID, 
        Min, Oreb, Pf, PlayerID, Pts, Reb, Stl, TeamID, Turnover)
        values {rnull(self.Ast, None)}, {rnull(self.Blk, None)}, {rnull(self.Dreb, None)},
        {rnull(self.Fg3Pct, None)}, {rnull(self.Fg3a, None)}, {rnull(self.Fg3m, None)},
        {rnull(self.FgPct, None)}, {rnull(self.Fga, None)}, {rnull(self.Fgm, None)}, {rnull(self.FtPct, None)}, 
        {rnull(self.Fta, None)}, {rnull(self.Ftm, None)}, {rnull(self.GameID, None)}, {rnull(self.Min, None)},
        {rnull(self.Oreb, None)}, {rnull(self.Pf, None)}, {rnull(self.PlayerID, None)}, 
        {rnull(self.Pts, None)}, {rnull(self.Reb, None)}, {rnull(self.Stl, None)}, {rnull(self.TeamID, None)}, 
        {rnull(self.Turnover, None)}
        """
        cn.cursor().execute(insert_statement)
        cn.connection().commit()

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
        self.Date = None
        self.HomeTeamID = None
        self.HomeTeamScore = None
        self.Period = None
        self.PostSeason = None
        self.Season = None
        self.Status = None
        self.Time = None
        self.VisitorTeamID = None
        self.TeamScore = None

#----------  
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.Game
        (ID, Date, HomeTeamID, HomeTeamScore, Period, PostSeason, Season, Status, Time, VisitorTeamID, 
        TeamScore)
        values ({self.ID}, '{rnull(self.Date, None)}', {rnull(self.HomeTeamID, None)},
        {rnull(self.HomeTeamScore, None)}, {rnull(self.Period, None)}, '{rnull(self.PostSeason, None)}',
        {rnull(self.Season, None)}, '{rnull(self.Status, None)}, '{rnull(self.Time, None)}', 
        {rnull(self.VisitorTeamID, None)}, {rnull(self.TeamScore, None)})
        """

        cn.cursor().execute(insert_statement)
        cn.connection().commit()

#---------- 
    def __str__(self):
        string = f"""ID: {self.ID}, Date: {self.Date}, HomeTeamID: {self.HomeTeamID}, 
        HomeTeamScore: {self.HomeTeamScore}, Period: {self.Period}, PostSeason: {self.PostSeason},
        Season: {self.Season}, Status: {self.Status}, Time: {self.Time}, VisitorTeamID: {self.VisitorTeamID}, 
        TeamScore: {self.TeamScore}\n"""
        return string

#----------
    def __repr__(self):
        string = f"""ID: {self.ID}, Date: {self.Date}, HomeTeamID: {self.HomeTeamID}, 
        HomeTeamScore: {self.HomeTeamScore}, Period: {self.Period}, PostSeason: {self.PostSeason},
        Season: {self.Season}, Status: {self.Status}, Time: {self.Time}, VisitorTeamID: {self.VisitorTeamID}, 
        TeamScore: {self.TeamScore}\n"""
        return string

