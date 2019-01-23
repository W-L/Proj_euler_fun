import numpy as np

def FUN(x):
    div=np.arange(1,x,1)
    factors=div[x%div==0]
    return(factors)
    
def is_prime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
    
    
def factors(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
                    
    
cnt=0
a=factors(600851475143)
for e in a:
    if is_prime(e)==True and e>cnt:
        cnt=e
    
print(cnt)

