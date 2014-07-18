# load original .csv from SQL to data master (dm) object
dm <- read.csv(file.choose())

# create vector of location codes
lc <- c(8824,7759,8215,8626,8213,8646,8647,8214,
        8825,8826,8823,7760,7685,7684,7694,8626,8115,8825,5160,5161,7758,5202)

for (i in lc)
{
    temp <- subset(dm, LocationCode==i)
    fname <- paste("Staff",i,".csv",sep="")
    write.csv(temp, file=fname, na="", row.names=FALSE)
}
