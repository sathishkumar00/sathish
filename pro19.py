rat=int(input())
gat=[]
for i in range(rat):
    li=[]
    li=list(map(int,input().split()))
    g.append(li)
 
fat=[]   
for i in gat:
    for j in i:
        f.append(j)
f.sort()
for i in fat:
    print(i,end=" ")
