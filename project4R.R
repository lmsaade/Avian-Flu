#Import packages
library(ggplot2)
library(dplyr)
library(magrittr)

#Read in egg data in csv format
egg_data <- read.csv("C:/Users/Lina/OneDrive/Documents/AIT 580/egg.csv")
print(egg_data)

#Change data type to date and check
egg_data %<>%
  mutate(Label = as.Date(Label, format = "%m/%d/%Y"))

print(egg_data)

#How are egg prices changing over time?
ggplot(egg_data, aes(x = Label, y = Value)) +
  geom_line() +
  ggtitle("Egg Prices Over Time") +
  labs(x = "Date", y = "Value in USD") +
  scale_x_date(date_labels = "%b %Y", date_breaks = "4 months")


  