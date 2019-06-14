ak=int(input())
bk=[]
xk=''
for i in range(ak):
    c=input()
    bk.append(c)
for i in range(ak-1):
    d=bk[i]
    e=bk[i+1]
    for y in range(len(min(bk,key=len))):
        if d[y]==e[y]:
            xk+=d[y]
        else:
            break
    bk.pop(i)
    bk.insert(0,xk)
    xk=''
print(bk[0])
