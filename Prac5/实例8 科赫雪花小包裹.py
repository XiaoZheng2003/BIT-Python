# 请在...补充一行或多行代码

import turtle
def koch(size, n):
    if not n:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main(level):
    #turtle.speed(10000)
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    
try:
    level = eval(input("请输入科赫曲线的阶: "))
    main(level)
except:
    print("输入错误")