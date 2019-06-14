import math
import functools
input11,input21=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(input21):
    ct,dt=map(int,input().split())
    temp=functools.reduce(math.gcd,List[ct-1:dt])
    print(temp)
