# install.packages('ISLR')
library ('ISLR')
# install.packages("tree")
library ('tree')
attach(Carseats)

High=ifelse(Sales<= 8, "No", "Yes")
Carseats <- data.frame(Carseats, High)
v <- tree(High ~ . -Sales, Carseats)
summary(v)
plot(v)
text(v, pretty=0)

View(Carseats)
