#####
#
# Sabermetrics 101 - Final Exam
#
# Matthew Sabban
# Working on the Final Exam
#
#####

# Import data
year_team <- read.csv(file.choose())

# Calculate AVG, SLG, OPS; then insert into data frame
year_team$AVG <- with(year_team, (H/(AB)))
year_team$OBP <- with(year_team, ((H+BB+HBP)/(AB+BB+HBP+SF)))
year_team$SLG <- with(year_team, ((H+X2B+2*X3B+3*HR)/(AB)))
year_team$OPS <- with(year_team, OBP + SLG)

# Correlation Plot Function
# Draws a scatter plot of 2 variables from a dataframe
# displaying a best-fit line and R^2 value in the legend
corr_plot <- function(v1, v2, df) {
  plot(df[[v1]], df[[v2]], xlab=v1, ylab=v2) # Draw scatter Plot
  linfit <- lm(df[[v2]]~df[[v1]]) # Calculate best-fit line
  abline(linfit) # Draw best-fit line
  # Add R^2 value in legend
  legend("topleft", legend = paste("R^2:", signif(summary(linfit)$r.squared, 4)))
}

# Add 1B for calculation simplicity
year_team$X1B <- with(year_team, H-X2B-X3B-HR)

# First we'll only use different types of hits
lin_basic_weights <- lm(R ~ X1B + X2B + X3B + HR, data=year_team)

# Apply model's coefficients to predict past runs
year_team$linRBasic <- predict(lin_basic_weights)

# Now let's add in BB, HBP, and SB to improve the regression's accuracy.
lin_more_weights <- lm(R ~ X1B + X2B + X3B + HR + I(BB + HBP) + SB, data=year_team)
year_team$linRMore <- predict(lin_more_weights)

#running correlation plots
corr_plot('HR', 'HR', year_team)
corr_plot('HR', 'HBP', year_team)
corr_plot('SF', 'R', year_team)