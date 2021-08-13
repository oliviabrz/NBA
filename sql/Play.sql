CREATE DATABASE `NBA` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

--TRUNCATE table NBA.Player
--TRUNCATE table NBA.Team

DELETE from NBA.Player;

DELETE from NBA.Team;

delete from NBA.Game
delete from NBA.PlayerGameStats 

select COUNT(*) from NBA.Team;

select * from NBA.Team

select * from NBA.Player

select * from NBA.Game

select * from NBA.PlayerGameStats 

select * from NBA.StatsAbbreviations 

select COUNT(*) from NBA.Player;

select COUNT(*) from NBA.PlayerGameStats;

select COUNT(*) from NBA.Game
where PostSeason = 0

select * from NBA.Game where ID = '444934';

insert into NBA.Team
(ID, Abbreviation, City, Conference, Division, FullName, Name)
values (1,'ab', 'ab', 'ab', 'ab', 'ab', 'ab')

select ID from NBA.Team where Abbreviation = 'LAC'

select ID from NBA.Team where Abbreviation = 'IND'

insert into NBA.Player
        (ID, FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID)
        values (2, 'Ike', 'Anigbogu', 'C', NULL, NULL, NULL, 1234) 
        
select p.FirstName, p.LastName, t.FullName 
from Player p
inner join Team t  
	on p.TeamID = t.ID 
where p.LastName = 'Antetokounmpo';

select p.FirstName, p.LastName, p.HeightFeet, p.HeightInches, p.WeightPounds, t.FullName 
from Player p
inner join Team t  
	on p.TeamID = t.ID 
where p.LastName = 'Morris'
and t.FullName in ('LA Clippers', 'Los Angeles Lakers');
--and (t.FullName = 'LA Clippers' or t.FullName = 'Los Angeles Lakers');

select p.FirstName, p.LastName, t.FullName, p.HeightFeet, p.HeightInches, p.WeightPounds
from Player p
inner join Team t 
	on p.TeamID = t.ID 
where p.LastName = 'Bryant' and t.Name = 'Lakers'

select p.FirstName, p.LastName, t.FullName as 'PlayerTeam', g.HomeTeamScore, g.VisitorTeamScore, pgs.*
from NBA.Game g
join PlayerGameStats pgs 
	on g.ID = pgs.GameID
join Player p
	on p.ID = pgs.PlayerID 
join Team t 
	on p.TeamID = t.ID 
where g.GameDate >= '2021-01-01' 
and p.FirstName = 'Joel'
and p.LastName = 'Embiid'
order by pgs.Min DESC 
--order by g.GameDate DESC 

select ID, FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID
        from NBA.Player p
        where p.FirstName = 'Joel' and p.LastName = 'Embiid'
        
        
SELECT FirstName
  FROM NBA.Player
 WHERE FirstName <> CONVERT(FirstName USING ASCII)       
 
SELECT * FROM performance_schema.session_variables
WHERE VARIABLE_NAME IN (
'character_set_client', 'character_set_connection',
'character_set_results', 'collation_connection'
) ORDER BY VARIABLE_NAME;

SHOW SESSION VARIABLES LIKE 'character\_set\_%';
SHOW SESSION VARIABLES LIKE 'collation\_%';

select ID, Abbreviation, City, Conference, Division, FullName, Name
from NBA.Team t
where t.Abbreviation = 'LAC'

SELECT Min, Fgm, Fg3m, Fga, Fg3a, Ftm, Fta, Oreb, Dreb, Reb, Ast, Stl, Blk,
	   Turnover, Pf, Pts, FgPct, FtPct, Fg3Pct, g.GameDate, g.Season, g.PostSeason 
FROM NBA.PlayerGameStats pgs 
join NBA.Game g 
	on pgs.GameID = g.ID 
where g.Season >= 2018
--select COUNT(*)

SELECT Blk, GameDate, PostSeason
        FROM NBA.PlayerGameStats pgs 
        join NBA.Game g 
	        on pgs.GameID = g.ID 
        where g.Season >= 2020
        order by GameDate DESC 
        
SELECT Count(*)
        FROM NBA.PlayerGameStats pgs 
        join NBA.Game g 
	        on pgs.GameID = g.ID 
        where g.Season >= 2020
        order by GameDate DESC 
        
SELECT DATE_FORMAT(GameDate, '%m-%Y') as StatDate, AVG(Min) as StatAvg
FROM  NBA.PlayerGameStats pgs 
        join NBA.Game g 
	        on pgs.GameID = g.ID 
        where g.Season = 2019
GROUP BY DATE_FORMAT(GameDate, '%m-%Y')


