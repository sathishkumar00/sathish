f=input()
f=f.split(" ")
g=f[0]
k=f[1]
a=list(g)
b=list(k)
h=j=0
d=a[0]
e=b[0]
for i in range(0,len(a)):
       if(a[i]==d and b[i]==e):
             h=h+1
       elif(a[i]!=d and b[i]==e):
             break
       elif(a[i]==d and b[i]!=e):
             break
       elif(a[i]!=d and b[i]!=e):
             d=a[i]
             e=b[i]
             h=h+1
       j=j+1
if(h==len(b)):
         print("yes")
else:
         print("no")
