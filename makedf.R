# Hawaii and West Virginia are not included

library(data.table)

setwd("C:/Users/lkim/Dropbox/Crime")
data <- data.frame()
s <- read.csv("us_states_hyph.csv.csv", header = FALSE, sep = ",")
s.abbrev <- s[,3]
s.abbrev <- s.abbrev[-(which(s.abbrev == "HI"))]
s.abbrev <- s.abbrev[-(which(s.abbrev == "WV"))]

a <- rep(s.abbrev, each = 9)
setwd("C:/Users/lkim/Dropbox/Crime/states_take2")
data <- data.frame(NULL)

# create one big dataframe with all the Google Trends Counts
for (file in dir())
{
  state <- as.data.frame(read.csv2(file, sep = ",", header = TRUE))
  state$Date <- as.Date(state$Date)
  state$Date<-format(state$Date,'%Y')
  state <- aggregate(.~Date, data = state, mean)
  state$guns.1 <- NULL
  state$guns.2 <- NULL
  state$guns.3 <- NULL
  data <- rbind.data.frame(data, state)
  print(dim(state))
}

data <- cbind(a, data)
write.csv(data, "crimecounts.csv")  # final dataset 

crime_stats <- read.csv("crime_df.csv")
data <- cbind(data, crime_stats)

########################################################################################
# start of data analysis
library(lme4)
plot(data)  # not seeing good linear relationship between response and the words 

fits <- lmList(data$x ~ data$felony + data$rape  | data$a, data=data)

library(lmerTest)
lmer(data$x ~ data$felony + data$rape  | data$a, data=data)

## try just california

cali <- data[which(data$a == "CA"),]
plot(cali)


