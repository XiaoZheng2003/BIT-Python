# 请在...补充一行或多行代码

def fbi(n):
    if n in [1,2]:
        return 1
    return fbi(n-1)+fbi(n-2)

n = eval(input())
print(fbi(n))