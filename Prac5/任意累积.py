# 请在...补充一行或多行代码

def cmul(*num):
    ans=1
    for i in num:
        ans*=i
    return ans

print(eval("cmul({})".format(input())))