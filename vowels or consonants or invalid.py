n=str(input())
L=["a","e","i","o","u","A","E","I","O","U"]
if n.isnumeric():
	print("invalid ")
elif n in L:
	print("vowels")
else:
	print("Consonant")
