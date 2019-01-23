is.prime <- function(n) n == 2L || all(n %% 2L:ceiling(sqrt(n)) != 0)

c<-1
l<-c()
while(c>0){
  if (is.prime(c)==TRUE){
    l<-append(l,c)
  }
  c<-c+1
  if (length(l)==10001){
    print(l[length(l)])
    break
  }
}