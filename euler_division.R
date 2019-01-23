
q<-c()
x<-1000
while (x>2){
  y<-strsplit(as.character(1/x),"")[[1]]
  if ((length(y)<17)&(y[3]==y[4])&(y[4]==y[5])){
    x<-x-1
    next
  }
  
  q<-append(q,as.numeric(capture.output(cat(y,sep=""))))
}