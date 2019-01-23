a="."
i=1
while len(a)<1000001:
    a=a+str(i)
    i+=1
    
sm=int(a[1])*int(a[10])*int(a[100])*int(a[1000])*int(a[10000])*int(a[100000])*int(a[1000000])
print(sm)