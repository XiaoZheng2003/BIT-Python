ans=0
for i in range(2,100):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        ans+=i
print(ans)