def ispent(a):
    n=((1+((1+24*(a)))**0.5)/6)
    if n == int(n):
        return True
    else:
        return False
        
def istri(a):
    n=((-1+((1+8*a))**0.5)/2)
    if n == int(n):
        return True
    else:
        return False
        
def ishex(a):
    n=(1+((1+8*a)**0.5))/4
    if n == int(n):
        return True
    else:
        return False
            
cnt=40756
while True:
    if ispent(cnt) == True and istri(cnt)==True and ishex(cnt)==True:
        print(cnt)
        break
    cnt+=1
    