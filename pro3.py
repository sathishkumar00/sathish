num1,num2=input().split()
ten=abs(len(num1)-len(num2))
for i in range(len(num1)):
    if len(num2)==1 and num2[i] in num1:
        break
    if num1[i]!=num2[i]:
        ten+=1
print(ten)
