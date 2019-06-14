def union(arr,count):
    sk=[]
    for i in range(0,count):
        if i==arr[i]:
            if arr[i] not in sk:
                sk.append(arr[i])
    if len(sk)>0:
        sk.sort()
        for i in range(len(sk)):
            print(sk[i],end=' ')
    else:
        print("-1")
size=int(input())
arr=list(map(int,input().split()))
count=len(arr)
union(arr,count)
