#Baseball Working Queries 


#On Base Percentage Query - ANGELS 2014

select ((SUM(H)+SUM(BB)+SUM(HBP)))/(SUM(AB)+SUM(SF)+SUM(BB)+SUM(HBP)) as AngelsOBP from Batting where teamID = 'LAA' and yearID = 2014;


#Battery AVG Query - ANGELS 2014

select (SUM(H)/SUM(AB)) as AngelsAVG from Batting where teamID = 'LAA' and yearID = 2014;