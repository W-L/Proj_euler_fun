FUN <- function(x) {
  x<-as.integer(x)
  div<-1:x
  factors<-div[x%%div==0]
  return(factors)
}

TRI <- function(x) {
  for (e in 1:x){
    y<-y+e
  }
  return(y)
}

x<-1
while (x<10000){
  z<-TRI(x)
  w<-length(FUN(z))
  if (w>499){
    print(z)
    break
  }
  x<-x+1
}
