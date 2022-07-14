flag=0
for i in range(100,1000):
    a,b,c=i%10,i//10%10,i//100
    if a**3+b**3+c**3==i:
        print("{}{:d}".format(',' if flag else '',i),end='')
        flag=1