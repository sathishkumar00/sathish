tan=int(input())
san=list(map(int,input().split()))
nan=g=[]
for i in range(0,tan):
    nan=list(bin(san[i]))
    nan=nan[2:]
    g.append(nan)
g=sorted(g)
g=g[::-1]
for i in range(0,tan):
    yan=1
    zan=0
    for j in range(len(g[i])-1,-1,-1):
        zan=zan+(int(g[i][j])*yan)
        yan=yan*2
    print(zan)
