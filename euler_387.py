import itertools

flatten_iter = itertools.chain.from_iterable

def FUN(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))
                    
def isprime(a):
    if len(FUN(a))==2:
        return True
    else:
        return False
        
def digsum(a):
    b=0
    for i in str(a):
        b=int(b)+int(i)
    return b
    
def harshad(a):
    if digsum(a) in FUN(a):
        return True
    else:
        return False
        
def rtrunc(a):
    c=str(a)[:-1]
    b=len(c)
    while b>0:
        if harshad(int(c))==True:
            b-=1
            c=c[:-1]
            if b==0:
                return True
            continue
        else:
            return False
    
def isstrong(a):
    b=digsum(a)
    c=a/b
    if isprime(c)==True:
        return True
    else:
        return False
        
cnt=10
tot=0
while cnt< 10**14:
    if isprime(cnt)==False:
        cnt+=1
        continue
    else:
        b=int(str(cnt)[:-1])
        if harshad(b)==True:
            if isstrong(b)==True:
                if rtrunc(b)==True:
                    tot=tot+cnt
                    cnt+=1
                    continue
                else:
                    cnt+=1
                    continue
            else:
                cnt+=1
                continue
        else:
            cnt+=1
            continue

print(tot)  
