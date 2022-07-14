h,m=eval(input())
BMI=m/(h**2)
print("BMI数值为:{:.2f}".format(BMI))
RESULT=("偏瘦","正常","偏胖","肥胖")
glo,nat=0,0
if BMI<18.5:
    glo,nat=0,0
elif BMI<24:
    glo,nat=1,1
elif BMI<25:
    glo,nat=1,2
elif BMI<28:
    glo,nat=2,2
elif BMI<30:
    glo,nat=2,3
else:
    glo,nat=3,3
print("BMI指标为:国际'{}',国内'{}'".format(RESULT[glo],RESULT[nat]))
