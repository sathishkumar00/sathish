Nk=int(input())
ak=list(map(int,input().split()))
c=[]
count=0
for i1 in ak:
  if i1 not in c:
    c1.append(i1)
for j1 in c:
  for k1 in ak:
    if(j1==k1):
      count=count+1
  if(count==1):
    print(j1)
  count=0
