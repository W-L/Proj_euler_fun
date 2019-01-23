
def hypotenuse(a,b):
    c=(((a**2)+(b**2))**(0.5))   
    return c
    
def isint(a):
    if a == int(a):
        return True
    else:
        return False
    
a=1
b=1
c=hypotenuse(a,b)
perim_list=[0,]*10000

while True:
    c=hypotenuse(a,b)
    if isint(c)==True:
        p=int(a+b+c)
        perim_list[p]+=1
    a+=1
    if a==1000:
        a=1
        b+=1
        if b==1000:
            break
    
perim_list=perim_list[:1001]
q=max(perim_list)
print(perim_list.index(q))
