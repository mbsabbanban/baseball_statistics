#Baseball Working Queries 

select * from Teams; 


#On Base Percentage Query - ANGELS 2014

select AVG((H+BB+IBB)/AB) as AngelsOBP from Batting where teamID = 'LAA' and yearID = 2014 AND AB >=10;


#Battery AVG Query - ANGELS 2014

select H/AB as AngelsAVG from Batting where teamID = 'LAA' and yearID = 2014;