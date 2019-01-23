import itertools

flatten_iter = itertools.chain.from_iterable

def FUN(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))
    
tr=1
add=2
while True:
    if len(FUN(tr))>500:
        print(tr)
        break
    tr=tr+add
    add+=1
