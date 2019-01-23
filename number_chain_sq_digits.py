def sq(a):
    b=str(a)
    newnum=0
    for i in b:
        c=int(i)**2
        newnum=newnum+c
    return newnum
    
def walk(a):
    while True:
        step=sq(a)
        if step == 1:
            return 1
        if step == 89:
            return 89
        a=step
        
cnt=1
total=0
while cnt < 10**7:
    a=walk(cnt)
    if a == 89:
        total+=1

    cnt+=1

print(total)

        