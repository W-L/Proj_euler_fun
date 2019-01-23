a<-c(1,2)
e<-1
while (max(a)<4000000){
  a<-append(a,a[e]+a[e+1])
  e<-e+1
}
a<-a[-length(a)]

b<-c()
for (i in a){
  if (i%%2==0){
    b<-append(b,i)
  }
}
sum(b)
