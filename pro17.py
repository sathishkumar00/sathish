man,san=map(int,input().split())
array=list(map(int,input().split()))
ran=0
for i in range(len(array)):
	for j in range(i+1,len(array)):
		if (array[i]+array[j]==san):
			ran+=1
			break
if(ran):
	print("yes")
else:
	print("no")
