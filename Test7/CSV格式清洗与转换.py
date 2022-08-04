f=open("data.csv")
lines=f.readlines()
ans=[]
for line in lines:
    ls=line.strip('\n').replace(' ','').split(',')
    ls=ls[::-1]
    ans.append(';'.join(ls))
for i in range(len(ans)-1,-1,-1):
    print(ans[i])