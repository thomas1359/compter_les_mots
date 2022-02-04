def occurence(t):
    d={}
    for x in t:
        if x in d:
            d[x]=d[x]+1
        else:
            d[x]=1
    return d

f=open("pg4791.txt",encoding="utf8")
texte = f.read().split()
f.close
lavé=[""]*len(texte)
for j in range(len(texte)):
    lavé[j]=texte[j].strip(',.!;?-')

comptage =occurence(lavé)
mot=""
max=1
res=[]
for k in comptage.keys():
    res.append((comptage[k],k))
res.sort()
print(res)
