barplot(unique(Data$Followers), 
        names.arg = unique(Data$Artist), 
        las = 2,
        cex.names = 0.25)

plot(Data$Tempo,Data$BPM, xlab="Tempo (Spotify)", ylab="Beats Per Minute (The Echo Nest)")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Tempo, xlab="Release Date", ylab="Tempo in BPM")

plot(Data$Noise,Data$Loudness, xlab="Spotify Value", ylab="The Echo Nest Value")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Noise, xlab="Release Date", ylab="Loudness")

barplot(table(Data$Key), xlab="Key Value", ylab="Frequency")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Weeks.until.appearance, xlab="Release Date", ylab="Weeks Until Reaching Top 10")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Danceability, xlab="Release Date", ylab="Danceability")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Energy, xlab="Release Date", ylab="Energy")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Valence, xlab="Release Date", ylab="Valence")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Seconds, xlab="Release Date", ylab="Length in Seconds")

plot(as.Date(Data2$Release.date, format = "%m/%d/%Y"), Data2$Key, xlab="Release Date", ylab="Key")
