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
pf_all <- within(pf_all, levels(home)[levels(home)=='FLO'] <- 'MIA')
pf_all <- within(pf_all, levels(visitor)[levels(visitor)=='FLO'] <- 'MIA')

#Now that the names have been corrected, can begin writing the function
#This will be the function for determining Park Factors

pf_stat_teams <- function(stat, data, season_year=2013) {
  
  
  data <- subset(data, year == season_year)
  
  home_stat = paste("home", stat, sep="_")
  
  visitor_stat = paste("visitor", stat, sep="_")
  
  pf_stat = paste("pf", stat, season_year, sep="_")
  
  cols = c(home_stat, visitor_stat, "home_ab", "visitor_ab")
  
  park_sums <- ddply(data, .(home), colwise(sum, cols))
  
  away_sums <- ddply(data, .(visitor), colwise(sum, cols))
  
  park_sums$park_ratio <- (park_sums[[home_stat]] + park_sums[[visitor_stat]]) / (park_sums[["home_ab"]] + park_sums[["visitor_ab"]])
  
  away_sums$away_ratio <- (away_sums[[home_stat]] + away_sums[[visitor_stat]]) / (away_sums[["home_ab"]] + away_sums[["visitor_ab"]])
  
  pf <- merge(park_sums, away_sums, by.x="home", by.y="visitor")
  
  pf[[pf_stat]] <- with(pf, pf$park_ratio / pf$away_ratio)
  
  pf <- rename(pf, replace=c("home" = "team"))
  
  pf <- subset(pf, select = c("team", pf_stat))
  
  return(pf)
  
}

hr_2013 <- pf_stat_teams("hr", pf_all, season_year=2013)
double_2010 <- pf_stat_teams("2b",pf_all, season_year=2010)
bb_2013 <- pf_stat_teams("bb",pf_all, season_year=2013)