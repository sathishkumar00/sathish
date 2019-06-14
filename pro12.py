nat,qat=map(int,input().split())
tat=list(map(int,input().split()))
st=[]
for i in range(qat):
    st.append(list(map(int,input().split())))
for i in st:
  z=0
  for j in range(i[0]-1,i[1]):
      z=z+tat[j]
  print(z)    
