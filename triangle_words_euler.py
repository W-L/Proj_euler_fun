from string import ascii_uppercase

infile="/home/lukas/Schreibtisch/words.txt"
inp=open(infile)
words=inp.read()
wordlist=words.split(",")
alph=ascii_uppercase

def wordscore(a):
    score=0
    for e in a:
        if e in alph:
            score=score+(alph.index(e)+1)
    return score
    
tri=[]
tr=1
add=2
while tr<250:
    tri.append(tr)
    tr=tr+add
    add+=1
    
total=0
for e in wordlist:
    if wordscore(e) in tri:
        total+=1
    
