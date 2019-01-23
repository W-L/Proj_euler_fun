a<-999
b<-999
l<-c()
while(a>99){
  p<-as.numeric(strsplit(as.character(a*b),"")[[1]])
  if (identical(p,rev(p))==TRUE){
    q<-as.numeric(capture.output(cat(p,sep="")))
    l<-append(l,q)
  }
  a<-a-1
  if (a==100){
    b<-b-1
    a<-999
    
  }
  if(b==100){
    print(max(l))
    break
  }
}


