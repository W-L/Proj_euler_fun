import itertools

flatten_iter = itertools.chain.from_iterable

def FUN(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))

def relPrime(x,y):
    l=[]
    fac_x=FUN(x)
    fac_y=FUN(y)
    for e in fac_x:
        if e in fac_y:
            l.append(e)
    f=len(l)
    if f ==1:
        return 1 
    else:
        return 0
    
def nover(x):
    n=0
    i=x-1    
    while i >0:
        if relPrime(x,i)==1:
            n+=1
        i=i-1
    o=x/n
    return o
        
leader=0
max_a=0
curr=2
while curr < 1000000:
    a=nover(curr)
    if a > max_a:
        max_a=a
        leader=curr
    curr+=1

