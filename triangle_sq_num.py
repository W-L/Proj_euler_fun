#triangle square number
import math

iters=1000000
sq_list=[0,]*0
tr_list=[0,]*0
n=0
n_tr=0
forever=0

while forever==0:
	if math.sqrt(n).is_integer():
		sq_list.append(n)
		n+=1

	if n > iters:
		n=0
		forever+=1	

	else:
		n+=1
		continue
		
while forever==1:
	n_tr=(n*(n+1))/2

	if n_tr.is_integer():
		tr_list.append(n)
		n+=1
	
	if n > iters:
		forever+=1

	else:
		n+=1
		continue

matches=sorted(set(tr_list).intersection(sq_list))
print(matches)

ptn=[0,]*0

for element in matches:
	q=element/4
	r=math.sqrt(q)
	ptn.append(r)

print(ptn)