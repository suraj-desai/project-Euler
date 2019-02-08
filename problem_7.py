import math
count=1
n=3
A=[2]
while count<10001:
    p=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            break
        else:
            p=p+1
    if p==int(math.sqrt(n)):
        count=count+1
    n=n+2
print(n-2)
        
    
