f=open("latex.log")
cnt=0
d={}
for line in f:
    for c in line:
        cnt+=1
        if c>='a' and c<='z':
            d[c]=d.get(c,0)+1
print("共{}字符".format(cnt),end='')
for i in range(26):
    t=chr(ord('a')+i)
    if t:
        print(",{}:{}".format(t,d[t]),end='')