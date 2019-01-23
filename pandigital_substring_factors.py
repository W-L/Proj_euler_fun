import numpy as np

def FUN(x):
    div=np.arange(1,x,1)
    factors=div[x%div==0]
    return(factors)
    
    
def subst(x):
    i=1
    lst=[0,2,3,5,7,11,13,17]
    while True:
        y=str(x)
        z=y[i:(i+3)]
        a=int(z)
        facs=FUN(a)
        if lst[i] in facs:
            i+=1
            if i==8:
                return True
                break
        else:
            return False
            break
        
        
dig=[0,1,2,3,4,5,6,7,8,9]

sm=0
cnt=0
tot_lst=[]
while cnt<1000000:
    pan=np.random.choice(dig,10,replace=False)
    pan="".join([str(pan[0]),str(pan[1]),str(pan[2]),str(pan[3]),str(pan[4]),str(pan[5]),str(pan[6]),str(pan[7]),str(pan[8]),str(pan[9])])
    pan=int(pan)
    if pan in tot_lst:
        continue
    tot_lst.append(pan)
    
    if subst(pan)==True:
        sm=sm+pan
    cnt+=1
                        