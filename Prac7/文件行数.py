f=open("latex.log")
cnt=0
for line in f:
    line=line.strip('\n')
    if len(line):
        cnt+=1
print("共"+str(cnt)+"行")