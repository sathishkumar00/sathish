xx,yy=map(int,input().split())
l=[]
for i in range(xx,yy+1):
    cd=0
    for j in range(1,i+1):
        if(i%j==0):
            cd=cd+1
    if(cd==2):
        l.append(xx)
print(len(l))  
