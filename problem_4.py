n=998001
p=0
while n>0:
    temp=n
    rev=0
    while temp>0:
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    if rev==n:
        for i in range(10,1000):
            if rev%i==0 and (rev//i)>=100 and (rev//i)<1000:
                p=1
    if p==1:
        break
    n=n-1
print(rev)
