num=eval(input())
str="Hello World"
if num==0:
    print(str)
elif num<0:
    for c in str:
        print(c)
else:
    for i in range(0,len(str)-1,2):
        print(str[i],str[i+1],sep='')
    print("d")