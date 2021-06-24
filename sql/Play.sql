--TRUNCATE table NBA.Player

DELETE from NBA.Player 

select COUNT(*) from NBA.Team;

select COUNT(*) from NBA.Player;

select * from NBA.Team

select * from NBA.Player 

select ID from NBA.Team where Abbreviation = 'LAC'

insert into NBA.Player
        (ID, FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID)
        values (2, 'Ike', 'Anigbogu', 'C', NULL, NULL, NULL, 1234) 
        
select p.FirstName, p.LastName, p.HeightFeet, p.HeightInches, p.WeightPounds, t.FullName 
from Player p
inner join Team t  
	on p.TeamID = t.ID 
where p.LastName = 'Morris'
and t.FullName in ('LA Clippers', 'Los Angeles Lakers');
--and (t.FullName = 'LA Clippers' or t.FullName = 'Los Angeles Lakers');




