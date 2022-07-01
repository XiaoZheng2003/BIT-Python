TempStr=input()
if TempStr[0:3]=='RMB':
    print("USD{:.2f}".format(eval(TempStr[3:])/6.78))
elif TempStr[0:3]=='USD':
    print("RMB{:.2f}".format(eval(TempStr[3:])*6.78))