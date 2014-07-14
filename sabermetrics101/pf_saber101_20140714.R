#####
#
# Sabermetrics 101 - PS6
#
# Matthew Sabban
# Determining Park Factors
#
#####

#Choosing the file location to create the initial data set
rox <- read.csv(file.choose())

#Creating subset data frames for home and visitor
park <- subset(rox, home == "COL")
away <- subset(rox, visitor == "COL")

#Creating the ratios for home and away homeRuns at Coors
# So HR/AB for both the home and away teams
park_ratio <- sum(park$home_hr + park$visitor_hr) / sum(park$home_ab + park$visitor_ab)
away_ratio <- sum(away$home_hr + away$visitor_hr) / sum(away$home_ab + away$visitor_ab)

#Calculating the ParkFactor
#Formula: 100 * (park_ratio/away_ratio)
pf_stat = 100 * (park_ratio/away_ratio)

#####

#Now I'm going to be using a similar formula to create a pf_stat function for a wider dataset

#Choosing the file location to create the initial data set
pf_all <- read.csv(file.choose())

#Need to change the data for the Florida Marlins to Miami Marlins

