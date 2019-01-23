library(utils)

FUN <- function(x) {
  x <- as.integer(x)
  div <- seq_len(abs(x))
  factors <- div[x %% div == 0L]
  factors <- list(neg = -factors, pos = factors)
  return(factors)
}

PAIRS<- function(x) {
  a<-FUN(x)
  b<-as.vector(a[[2]])
  c<-combn(b,2)
  counter<-0
  for (i in 1:(length(c)/2)){
    e<-c[,i]
    if (e[2]%%e[1]==0)
      counter<-counter+1
  }
  return(counter)
}

is.prime <- function(n) n == 2L || all(n %% 2L:ceiling(sqrt(n)) != 0)

PRIMEPROD <- function(m) {
  x<-1
  y<-c()
  while(x>0){
    if (is.prime(x)){
      y<-append(y,x)
    }
    x<-x+1
    if (length(y)==m){
      p<-1
      for (e in y){
        p<-p*e
      }
      return(p)
      break
    }
  }
}


FINDE <- function(m,n) {
  a<-PAIRS(PRIMEPROD(m)**n)
  x<-a-1
  while (x>-1){
    b<-a/(2**x)
    if (all.equal(b,as.integer(b))==TRUE){
      return(x)
      break
    }
    x<-x-1
  }
}

y<-0
for (i in 1:8){
  x<-FINDE(904961,i)
  y<-y+x
}

FINDE(10,2)
a<-PRIMEPROD(10)**2
PAIRS(a)

PRIMEPROD(1000)
