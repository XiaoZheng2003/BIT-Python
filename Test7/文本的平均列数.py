f=open("latex.log")
lines,total=0,0
for line in f:
    line=line.strip('\n')
    if len(line):
        lines+=1
        total+=len(line)
print("{:.0f}".format(total/lines))