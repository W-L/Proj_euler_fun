import numpy as np

a=np.arange(2,101,1)
b=np.arange(2,101,1)

l=[]

for e in a:
    for f in b: 
        z=e**f
        if z not in l:
            l.append(z)
            
print(len(l))
print(len(set(l)))
