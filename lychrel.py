def rev(a):
    b=str(a)
    c=""
    for i in b:
        c="{}{}".format(i,c)
    d=int(c)
    return d

def is_pal(a):
    if a == rev(a):
        return True
    else:
        return False
        
def lych(a):
    cnt=1
    while True:
        a=a+(rev(a))
        if is_pal(a)==True:
            return False
            break
        else:
            cnt+=1
            if cnt ==50:
                return True
                break
            continue
        

counter=0
lychs=0
while counter<10000:
    if lych(counter)==True:
        lychs+=1
    counter+=1
    
print(lychs)