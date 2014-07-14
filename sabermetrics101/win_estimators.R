
#Lesson on trying to create models for Top Winning Teams
wpct_95th_pct = quantile(win_estimators$WPct, .95)
top_winners = win_estimators[win_estimators$WPct >= wpct_95th_pct, ]

splom(top_winners, xlab="Top 5th Percentile WPct")
#example correlations
cor(top_winners$WPct, top_winners$BJames_Pythag_WPctII)

#Creating an AL East Estimator and NL West Estimator
AL_East=c('BAL','BOS','NYA','TBA','TOR')
NL_West=c('ARI','COL','LAN','SDN','SFN')
AL_East_Estimator = win_estimators[win_estimators$teamID %in% AL_East,]
NL_West_Estimator = win_estimators[win_estimators$teamID %in% NL_West,]

#Creating the AL East Histogram
hist(AL_East_Estimator$WPct)

#Creating the NL West Histogram
hist(NL_West_Estimator$WPct)

#Calculating the Runs to Wins Conversion
# Basic Formula: x=avgRuns - sq(avgRuns^2/(1/(.500-1/162)-1))
# Exceptions:
# -Use Division Wpct Average
# -replace runs with runsAllowed

#AL_EAST&NLWest
r2W_AL= mean(AL_East_Estimator$R) - sqrt(mean(AL_East_Estimator$RA)^2 / (1 / (mean(AL_East_Estimator$WPct)-1/162)-1))

r2W_NL= mean(NL_West_Estimator$R) - sqrt(mean(NL_West_Estimator$RA)^2 / (1 / (mean(NL_West_Estimator$WPct)-1/162)-1))

