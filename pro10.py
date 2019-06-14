mam=int(input())
nan=[int(i) for i in input().split()]
xx=0
for i in range(mam):
	for j in range(i):
		if nan[j]<nan[i]:
			xx+=nan[j]
print(xx)
