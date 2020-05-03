barplot(projectdata$Population.Density, 
        ylim = c(0, 1300),
        names.arg = projectdata$State, 
        las = 2,
        cex.names = 0.6,main = "Graph 1: Artist Following")

plot(projectdata$High.School..,projectdata$Population.Density,main = "Graph 2: Echo Nest BPM versus Spotify API Tempo",xlab="Percentage of People with High School Education or Higher ", ylab="Population Density")

plot(projectdata$Bachelor.s.Degree..,projectdata$Population.Density,main = "Graph 3: Trend in BPM Over Time",xlab="Percentage of People with Four Year College Education or Higher ", ylab="Population Density")

plot(projectdata$Population.Density,projectdata$Median.Income,main = "Graph 4: Echo Nest versus Spotify API: Loudness",xlab="Population Density", ylab="Median Income")

plot(projectdata$Poverty,projectdata$Population.Density,main = "Graph 5: Trend in Loudness Over Time",xlab="Percentage of Impoverished People", ylab="Population Density")

barplot(projectdata$Population.Density, 
        ylim = c(0, 1300),
        names.arg = projectdata$State, 
        las = 2,
        cex.names = 0.6,main = "Graph 6: Key Frequency")

plot(projectdata$Without.health.insurance,projectdata$Population.Density,main = "Graph 7: Time from Release to Charting",xlab="Percentage of People Without Health Insurance", ylab="Population Density")

plot(projectdata$Non.white,projectdata$Population.Density,main = "Graph 8: Trend in Danceability Over Time",xlab="Percentage of Non-White People", ylab="Population Density")

plot(projectdata$Non.white,projectdata$Population.Density,main = "Graph 9: Trend in Energy Over Time",xlab="Percentage of Non-White People", ylab="Population Density")

plot(projectdata$Non.white,projectdata$Population.Density,main = "Graph 10: Trend in Valence Over Time",xlab="Percentage of Non-White People", ylab="Population Density")

plot(projectdata$Non.white,projectdata$Population.Density,main = "Graph 11: Trend in Song Length Over Time",xlab="Percentage of Non-White People", ylab="Population Density")