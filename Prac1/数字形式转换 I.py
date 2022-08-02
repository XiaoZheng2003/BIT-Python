CHAR="零一二三四五六七八九"
str=input()
for c in str:
    print(CHAR[eval(c)],end='')