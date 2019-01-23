def fp(x):
    y=str(x)
    s=0
    for i in y:
        s=s+(int(i)**5)
    if s==x:
        return 1
    else:
        return 0
            

cnt=2
sm=0
while cnt<2000000:
    po=fp(cnt)
    if po == 1:
        sm=sm+cnt
    cnt+=1