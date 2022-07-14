def day(df:int):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup*=0.99
        else:
            dayup*=1+df
    return dayup

ans=0
while day(ans)<37.78:
    ans+=0.001
print("工作日的努力参数是: {:.3f}".format(ans))