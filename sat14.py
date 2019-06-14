ak=int(input())
sk=list(map(int,input().split()))
y=sorted(s)[::-1]
z=""
if(sk==[0]*ak):
    print("0")
else:
    for j in y:
        z=z+str(j)
    print(int(z))
