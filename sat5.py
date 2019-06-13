sat=int(input())
sk=0
while(sat>0):
    cat=sat%10
    sk=sk*10+cat
    sat=sat//10
print("The reverse",sk)    
    
