num = int(input())
res = 0
for i in range(2,(num//2)+1):
    if(num%i == 0):
        res = res+1
        break
if(res == 0):
    print("is pirme")
else:
    print("is not prime") 


