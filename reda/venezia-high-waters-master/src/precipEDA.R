library(lattice)
pdata <- read.csv("../precipitationdata/DB_OSSERVATORIO_1985_1989.csv")
pdata1 <- read.csv("../precipitationdata/DB_OSSERVATORIO_1990_1994.csv")
#first(pdata)
#size(pdata[1])
#boxplot(coredata(pdata[1]))
multmerge <- function(mypath){
  filenames<-list.files(path=mypath, full.names=TRUE)
  datalist <-lapply(filenames, function(x){read.csv(file=x,header=T)})
  Reduce(function(x,y) {merge(x,y)}, datalist)
}

finaldata <- multmerge("../precipitationdata")
m = merge(pdata1, pdata)

#write.csv(m, file="testdataset.csv", row.names = FALSE)
