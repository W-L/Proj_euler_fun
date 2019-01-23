a<-1
l<-c()

while(a<1000000){
  e<-as.numeric(strsplit(as.character(a),"")[[1]])
  if (identical(e,rev(e))!=TRUE){
    a<-a+1
    next
  }
  
  b<-as.integer(rev(intToBits(a)))
  c<-capture.output(cat(b,sep=""))
  k<-substr(c,regexpr("[^0]",c),nchar(c))
  g<-as.numeric(strsplit(as.character(k),"")[[1]])
  
  if (identical(g,rev(g))==TRUE){
    l<-append(l,a)
  }
  a<-a+1
}
print(l)
sum(l)
