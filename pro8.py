Sat2=int(input())
lat1=list(map(int,input().split()))
count=0
for i in range(len(lat1)-2):
    for j in range(i+1,len(lat1)-1):
        for k in range(j+1,len(l1)):
            if lat1[i]<l1[j]<l1[k] and i<j<k:
                count=count+1
print(count)
