man=input()
jan=1
for i in range(len(man)-1):
    s=man[i]+man[i+1]
    p=int(s)
    if p<=26 and m[i]!="0":
        jan+=1
if jan==3:
    print(jan)
else:
    print(jan+(jan-1)//2)
