at,bt=map(int,input().split())
ma=list(map(int,input().split()))
tanq=[]
for i in range(0,bt):
    d = []
    d=list(map(int,input().split()))
    s = ma[d[0]-1]
    for j in range(min(d),max(d)):
        s=s^ma[j]
    tanq.append(s)
for i in range(0,len(tanq)):
    print(tanq[i])
