def mc(a):
    b=max(set(a),key=a.count)
    return b
    
def getVAL(a):
    val=[]
    cnt=0
    ind=0
    while cnt<5:
        v=a[ind]
        if v=="T":
            v=10
        if v=="J":
            v=11
        if v=="Q":
            v=12
        if v=="K":
            v=13
        if v=="A":
            v=14            
        val.append(int(v))
        ind=ind+3
        cnt+=1    
    return val
    
def getSUIT(a):
    suit=[]
    cnt=0
    ind=1
    while cnt<5:
        s=a[ind]
        suit.append(s)
        ind=ind+3
        cnt+=1
    return suit
    
def getHAND(a):
    val=getVAL(a)
    vallen=len(list(set(val)))
    if vallen == 4:
        return 2
    if vallen == 3:
        cntmax=0
        for i in range(1,15):
            cnt=val.count(i)
            if cnt > cntmax:
                cntmax=cnt
        if cntmax==2:
            return 3 
        if cntmax==3:
            return 4
    if vallen == 2:
        cntmax=0
        for i in range(1,15):
            cnt=val.count(i)
            if cnt > cntmax:
                cntmax=cnt
        if cntmax==3:
            return 7 
        if cntmax==4:
            return 8
    if vallen == 5:
        suit=getSUIT(a)
        suitlen=len(list(set(suit)))
        if suitlen != 1:
            val.sort()
            if val[4]-4==val[0] and val[3]-3 == val[0] and val[2]-2 == val[0] and val[1]-1 == val[0]:
                return 5
            else: 
                return 1
        if suitlen == 1:
            val.sort()
            if val[4]-4==val[0] and val[3]-3 == val[0] and val[2]-2 == val[0] and val[1]-1 == val[0]:
                valmax=max(val)
                if valmax == 14:
                    return 10
                if valmax != 14:
                    return 9
            else:
                return 6
                          
def decider(a):
    b=getHAND(a)    
    c=getVAL(a)
    if b==1 or b==5 or b==6 or b==9:
        dec=max(c)
    if b==2 or b==4 or b==7 or b==8 or b==3:
        dec=mc(c)
    return dec
        
def poker(a):
    p1hand=p1[a]
    p2hand=p2[a]
    p1score=getHAND(p1hand)
    p2score=getHAND(p2hand)
    
    if p1score > p2score:
        return 1
    if p1score < p2score:
        return 0
    if p1score==p2score:
        p1dec=decider(p1[a])
        p2dec=decider(p2[a])
        if p1dec > p2dec:
            return 1
        if p1dec < p2dec:
            return 0
        if p1dec == p2dec:
            print(p1[a],"///",p2[a])
            return 2

infile="/home/lukas/Schreibtisch/p054_poker.txt"
inp=open(infile)
hands=inp.readlines()
cnt=0
for i in hands:
    hands[cnt]=i.rstrip("\n")
    cnt+=1
    
p1=[]
p2=[]
while len(hands)>0:
    a=hands.pop(0)
    b=a[:14]
    c=a[15:]
    p1.append(b)
    p2.append(c)

wins=0
loss=0
tie=0

for i in range(0,len(p1)):
    out=poker(i)
    if out==1:
        wins+=1
    if out==0:
        loss+=1
    if out==2:
        tie+=1
        
print(wins+loss+tie)
   