nat = int(input())
kit = 1000
for i in range(0,20):
    if pow(2,i)<=nat:
        a = abs(pow(2,i)-nat)
        if a<=kit:
            kit=a
print(kit)
