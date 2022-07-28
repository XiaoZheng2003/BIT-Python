# 请在...补充一行或多行代码

def prime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return 0
    return 1

n = int(eval(input())+0.999)
cnt=0
while cnt<5:
    if(prime(n)):
        print((",{}" if cnt else "{}").format(n),end='')
        cnt+=1
    n+=1
