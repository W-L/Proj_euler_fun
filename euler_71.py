import itertools

flatten_iter = itertools.chain.from_iterable

def FUN(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))
                    
                    
def HCF(a,b):
    c=FUN(a)
    d=FUN(b)
    if a==b:
        return 0
    overlap=list(set(c).intersection(d))
    if len(overlap)==1:
        return 1
    else:
        return 0
     
a=1
b=2
l=dict()
while a<10000:
    if HCF(a,b)==1:
        l[a,b]=a/b
    b+=1
    if b>10000:
       a+=1
       b=a+1

li=sorted(l, key=l.get)
ind=li.index((1,3))
print(li[ind-1])

