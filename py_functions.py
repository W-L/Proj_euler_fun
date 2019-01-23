import numpy as np

def FUN(x):
    div=np.arange(1,x,1)
    factors=div[x%div==0]
    return(factors)
    
cnt=0
a=0
while a<10001:
    b=sum(FUN(a))
    c=sum(FUN(b))
    if c==a:
        if a!=b:
            cnt=cnt+a
    a+=1
    
    