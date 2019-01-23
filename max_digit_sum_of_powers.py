def qsum(x):
    nums=str(x)
    qs=0
    for i in nums:
        qs=qs+int(i)
    return qs
    
a=0
b=0

maxim=0

while a < 100:   
    while b < 100:
        x=a**b
        y=qsum(x)
        if y > maxim:
            maxim=y
            
        b+=1
    a+=1
    b=0