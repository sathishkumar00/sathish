sk=input()
sk=sk.split(" ")
g=sk[0]
k=sk[1]
sa=list(g)
b=list(k)
h=j=0
d=sa[0]
e=b[0]
for i in range(0,len(sa)):
       if(sa[i]==d and b[i]==e):
             h=h+1
       elif(sa[i]!=d and b[i]==e):
             break
       elif(sa[i]==d and b[i]!=e):
             break
       elif(sa[i]!=d and b[i]!=e):
             d=sa[i]
             e=b[i]
             h=h+1
       j=j+1
if(h==len(b)):
         print("yes")
else:
         print("no")
