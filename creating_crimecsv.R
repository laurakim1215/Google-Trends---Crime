# Hawaii and West Virginia are not included


library(xts)
setwd("C:/Users/lkim/Dropbox/Crime")

states <- read.csv("us_states_hyph.csv.csv", header = FALSE, sep = ",")
state.names <- states[,2]
state.names <- as.character(state.names)
state.abbrev <- states[,3]

crime.data <- read.csv("crime6616.csv", header = TRUE, sep = "," )
q <- crime.data[,1]

# replaces citiesstates with just state names
for (x in state.names){
   q <- sub(paste0(".*",x), x, q)
}

crime.data[,1] <- q
crime.data <- crime.data[,c(1,5:13)]
crime.data <- as.data.frame(crime.data)

# removes all rows with NA
df <- crime.data[complete.cases(crime.data),]
names(df) <- c("states", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012" )


# sum all the city level data to make it state level
crime_df <- aggregate(df[,2:10], list(df$states), sum)
crime_df <- crime_df[-47,]
crime_df_temp <- t(crime_df)
crime_df_temp <- crime_df_temp[-1,]
crime_df_final <- as.vector(crime_df_temp) 

write.csv(crime_df_final, "crime_df.csv", row.names = FALSE)
