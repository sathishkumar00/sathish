xat,yat=map(int,input().split())
mat=list(map(int,input().split()))
mat.sort()
mat.reverse()
s=y
zat=0
for i in mat:
    if(s>=i):
        no=int(s/i)
        zat=zat+no
        s=s-no*i
    if s==0:
        break
if(s==0):
   print(zat)
else:
   print("it's not posiible to select coins in such a way that they sum upto",S)        
