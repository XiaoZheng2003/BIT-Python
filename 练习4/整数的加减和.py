ans=0
for i in range(1,967):
    ans+=i if i%2 else -i
print(ans)