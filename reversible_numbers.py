def reverse(a):
    b=str(a)
    c=""
    for e in b:
        c=e+c
    return int(c)

def allodd(a):
    c=str(a)
    for d in c:
        if int(d)%2==0:
            return False
    return True

cnt=1
rev_nums=0
l=[]
while cnt < 1*10**8:
    str_cnt=str(cnt)   
    if int(str_cnt[0])%2 !=0 and int(str_cnt[-1])%2 !=0:
        cnt+=1
        continue
    if int(str_cnt[0])%2 ==0 and int(str_cnt[-1])%2 ==0:
        cnt+=1
        continue
    if int(str_cnt[-1])==0:
        cnt+=1
        continue
    if cnt==9000:
        cnt=100000
        continue
    if cnt==1000000:
        cnt=2000000
        continue
    if cnt==1*10**8:
        cnt=4*10**8
        continue
 

    rev_cnt=reverse(cnt)
    summ=cnt+rev_cnt
    
    if allodd(summ)==True:
        rev_nums+=1
        l.append(cnt)
        
        
    cnt+=1
    
    
    
print(rev_nums)
#print(l)
#print(720+18000+50000)
#0 bis M:18720
#M bis 10M 50000
#10m  bis 20m 108000
