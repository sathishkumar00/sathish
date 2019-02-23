p,s=map(int,input().split())
y=[]
for i in range(p+1,s):
if(i%2==0):
y.append(i) 
print(*y)   
