#not solved

is.prime <- function(n) n == 2L || all(n %% 2L:ceiling(sqrt(n)) != 0)


x1<-600851475143
x<-10000000
d<-x-1
f<-c()
while (d<x){
  if (d%%2==0){
    d<-d-1
    next
  }
  if (is.prime(d)==TRUE){
    z<-x/d
    if (all.equal(z, as.integer(z),tolerance=1e-50)==TRUE){
      print(d)
      break
    }
  }
  d<-d-1
}

