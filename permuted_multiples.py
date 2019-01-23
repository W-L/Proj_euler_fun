def crush(a):
    b=list(str(a))
    b.sort()
    c="".join(map(str,b))
    d=int(c)
    return d
    
    
cnt=1
i=2
while True:
    if crush(cnt)==crush((cnt*i)):
        i+=1
        if i==7:
            print("done")
            print(cnt)
            break
    else:
        cnt+=1