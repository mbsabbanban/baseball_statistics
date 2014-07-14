###########
# SABR 101x
#

# Read in file of Retrosheet Gamelog data
attendance_data <- read.csv(file.choose())
summary(attendance_data)
attach(attendance_data)

#Game_logs = attendance_data[c("attendance", "game_minutes", "home_score")]
#splom(Game_logs, xlab="Retrosheet Gamelogs Scatterplot Matrix")

#
####Part of the assignment
#
#attendance_data$total_runs <- with(attendance_data, home_score, + visitor_score)
total_runs <- with(attendance_data, home_score + visitor_score)
attendance_data["total_runs"] <- total_runs

total_time_data <- attendance_data[c('game_minutes', 'total_runs', 'outs')]

require('lattice')
splom(total_time_data)

cor(game_minutes, outs)
plot(total_runs, outs)

projected_minutes <- lm(game_minutes ~ total_runs + outs)

#
###Part 2 of the Assignment
#

attendance_data$RedSox_playing <- with(attendance_data, ifelse(home == 'BOS' | visitor == 'BOS', 1, 0))

#Creating a subset dataframe just for the Red Sox
RedSox_games <- attendance_data[attendance_data$RedSox_playing == 1,]

summary(RedSox_games)
hist(RedSox_games$total_runs, breaks = 40)

#
###Part 3 of the Assignment
#

#Creating Variables for the Umpires
attendance_data$BrianGorman <- with(attendance_data, ifelse(hp_ump_name == 'Brian Gorman', 1, 0))
attendance_data$JimJoyce <- with(attendance_data, ifelse(hp_ump_name == 'Jim Joyce', 1, 0))
attendance_data$DaleScott <- with(attendance_data, ifelse(hp_ump_name == 'Dale Scott', 1, 0))
attendance_data$TimWelke <- with(attendance_data, ifelse(hp_ump_name == 'Tim Welke', 1, 0))

BrianGorman_games <- attendance_data[attendance_data$BrianGorman == 1,]
JimJoyce_games <- attendance_data[attendance_data$JimJoyce == 1,]
DaleScott_games <- attendance_data[attendance_data$DaleScott == 1,]
TimWelke_games <- attendance_data[attendance_data$TimWelke == 1,]

###

#With the above data, we're going to run a multivariate regression
# **NOTE this is just example: Projected_Attendance <-lm(attendance_data$attendance ~ total_runs)
projected_runs <-lm(attendance_data$total_runs ~ attendance_data$RedSox_playing + attendance_data$BrianGorman + attendance_data$JimJoyce + attendance_data$DaleScott + attendance_data$TimWelke)

summary(projected_runs$total_runs)
confint(projected_runs, level = 0.95)