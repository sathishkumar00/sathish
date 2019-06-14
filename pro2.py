from itertools import combinations
letr1,numb1=map(int,input().split())
numb2=len(str(letr1))
aa=list(combinations(str(letr1),numb2-numb1))
aa=(sorted(aa))
bb="".join(aa[0])
print(bb)
