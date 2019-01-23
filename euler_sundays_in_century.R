d<-vector(length=(100*365+25))
w<-length(d)/7
for (i in 1:w){
  d<-replace(d,i*7,1)
}

sundays<-d

ja<-31
fb<-28
mr<-31
ap<-30
my<-31
jn<-30
jl<-31
au<-31
sp<-30
oc<-31
nv<-30
dc<-31

c<-c()
for (e in 1:100){
  c<-append(c,1)
  for (f in 2:ja-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  if ((1900+e)%%4!=0){
    for (g in 2:fb-1) {
      c<-append(c,0)  
    }
  } else {
    for (h in 1:28) {
      c<-append(c,0)  
    }
  }
  
  c<-append(c,1)
  for (z in 2:mr-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (j in 2:ap-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (k in 2:my-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (l in 2:jn-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (m in 2:jl-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (n in 2:au-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (o in 2:sp-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (p in 2:oc-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (q in 2:nv-1) {
    c<-append(c,0)  
  }
  
  c<-append(c,1)
  for (r in 2:dc-1) {
    c<-append(c,0)  
  }
}
firsts<-c

counter<-0
for (element in 1:length(sundays)){
  if ((sundays[element]==1)&(firsts[element]==1)){
    counter<-counter+1
  }
}
print(counter)

# 1 sunday too much
