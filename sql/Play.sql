--TRUNCATE table NBA.Player
--TRUNCATE table NBA.Team

DELETE from NBA.Player;

DELETE from NBA.Team;

delete from NBA.Game
delete from NBA.PlayerGameStats 

select COUNT(*) from NBA.Team;

select * from NBA.Team

select * from NBA.Player

select COUNT(*) from NBA.Player;

select COUNT(*) from NBA.PlayerGameStats;

select COUNT(*) from NBA.Game;

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



© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
