NAME,PWD="Kate","666666"
cnt=0
while cnt<3:
    name=input()
    pwd=input()
    if name==NAME and pwd==PWD:
        print("登录成功！")
        exit()
    else:
        cnt+=1
print("3次用户名或者密码均有误！退出程序。")