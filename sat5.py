sat=int(input())
bat=0
while(sat>0):
    cat=sat%10
    bat=bat*10+cat
    sat=sat//10
print("The reverse",bat)    
    
