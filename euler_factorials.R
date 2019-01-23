x<-3
l<-c()
while (x>0){
  y<-as.numeric(strsplit(as.character(x),"")[[1]])
  z<-factorial(y)
  a<-sum(z)
  if (a==x){
    l<-append(l,x)
  }
  x<-x+1
}


