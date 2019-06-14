sa,n=map(int,input().split())
pa=list(map(int,input().split()))
zz=[]
for i in range(0,n):
    f=[]
    f=list(map(int,input().split()))
    m=f[0]
    for j in range(min(f)-1,max(f)):
        if m>pa[j]: m=pa[j]
    zz.append(m)
for i in range(0,len(zz)):
    print(zz[i])
