flag=0
for i in range(1000,10000):
    a,b,c,d=i%10,i//10%10,i//100%10,i//1000
    if a**4+b**4+c**4+d**4==i:
        print(i)