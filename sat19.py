nandy=int(input())
sathish=list(map(int,input().split()))
for i in sathish:
    if sathish.count(i)>1:
        print(i)
        break
else:
    print("unique")
