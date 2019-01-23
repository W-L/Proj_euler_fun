import numpy as np

def collatz(x):
    cnt=1
    while cnt>0:
        if x%2==0:
            x=x/2
            cnt+=1
            if x==1:
                return int(cnt)
                break
            else:
                continue
        else:
            x=(3*x)+1
            cnt+=1
            continue


t=0
curr=0
l=np.arange(1,1000000,1)

for y in l:
    z=collatz(int(y))
    if z > t:
        t=z
        curr=y


