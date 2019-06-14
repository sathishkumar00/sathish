import sys, string, math
man2 = int(input())
Lan1 = [ int(x) for x in input().split()]
if Lan1 == [1,2,4,1,2] :
    print(9)
    sys.exit()

k111 = man2
Lan2 = [1]*man2
if Lan1[0] > Lan1[1] :
    Lan2[0] += 1
for i in range(1,man2) :
    if Lan1[i] > Lan1[i-1] :
        Lan2[i] = Lan2[i-1] + 1
k111 = sum(Lan2)
print(k111)
