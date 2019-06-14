ff=input()
ff=ff.split(" ")
gg=ff[0]
hh=ff[1]
for i in range(0,len(gg)):
        c=0
        if(gg[i]!=hh[i]):
             c=c+1
if(c==1):
     print("yes")
else:
     print("no")
