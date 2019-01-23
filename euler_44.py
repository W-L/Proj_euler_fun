
def pentagon(a):
    p_a=a*(3*a-1)/2
    return p_a

def sum_dif(a):
    for i in p_l:
        p_diff=a-i
        if p_diff in p_l:
            p_sum=[a+i,p_diff]
            return p_sum
            break
    return False

def ispent(a):
    n=((1+((1+24*(a)))**0.5)/6)
    if n == int(n):
        return True
    else:
        return False
    
cnt=1
p_l=[]
while True:
    p_c=pentagon(cnt)
    p_l.append(p_c)
    outc=sum_dif(p_c)
    if outc != False:
        sol=ispent(outc[0])
        if sol == True:
            print(outc[1])
            break
        else:
            cnt+=1
            continue
    else:
        cnt+=1
        
