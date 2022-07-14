from random import seed,random
seed(123)
n=eval(input())
cnt=0
for i in range(n):
    x,y=random(),random()
    if x**2+y**2<=1.0:
        cnt+=1
print("{:.6f}".format(4*cnt/n))