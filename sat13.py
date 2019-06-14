K12=int(input())
n12=list(map(int,input().split()))
li=[]
for x in range(K12):
    for i in range(x+1,len(n12)):
        if(n12[i]==n12[x]):
          li.append(n12[x])
if (len(li)==0):
    print("unique")
else:
    li.sort()
    li2=set(li)
    for x in li2:
        print(x,end=" ")
