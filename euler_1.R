x<-1
y<-c()
while (x<1000){
  z<-x/3
  if (all.equal(z, as.integer(z))==TRUE){
    y<-append(y,x)
  }
  x<-x+1
}

a<-1
while (a<1000){
  z<-a/5
  if (all.equal(z, as.integer(z))==TRUE){
    y<-append(y,a)
  }
  a<-a+1
}
length(y)
r<-unique(y)
length(r)
sum(r)
