baseball_statistics
===================

My repository for everything and anything baseball related

#####

Baseball Project - Daily wOBA Tracker

wOBA is "Weighted On Base Average", this is perhaps the most telling statistic to measure a player's overall offensive contribution per plate appearance
More info can be found here: (http://en.wikipedia.org/wiki/WOBA)

For now, this project will focus on tracking stats for the New York Mets (Because GOOOOOO METSSSSSS!!!) but will eventually expand this tool so that it'll spit out a daily report for all of the other teams.

The purpose of this project is to track individual player stats of the Mets, give an overall wOBA for the Mets as a whole, and expand this tool with other useful statistics that would be very good to know. I hope to not only improve my python skills, but also to improve my familiarity with Git/Github and most importantly, further improve my understanding of the wonderful sport known as Baseball.

# Where to find
Original Fork can be found here:
https://github.com/mbsabbanban/baseball_statistics.git

All modifications are currently being made on this fork:
https://github.com/pibarra_2010/baseball_statistics.git

# Important Scripts

local_player_stat_get.py (Local version, testing purposes. Can possibly be deleted)
local_rawdata_stat_get.py (Local version, testing purposes. Can possibly be deleted)
rawdata_stat_get.py (Was working at some point, needs to be QA'd)
wOBA_stat_get.py (Unfinished)

#####

# Required Libraries

Additional notes for a Windows User

(1) Make sure that you install Python on your Windows machine (I found http://learnpythonthehardway.org/book/ex0.html helpful for setting up) // [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python34", "User")
(2) You need to download Beautiful Soup 4 package if you don't have it already. If you're using Python 3.4, 'pip' is already included in the package. Just type 'pip install beautifulsoup4' from the shell
(3) You also need to install pymysql. 'pip install pymysql'
>>>