s=input()
for i in s:
    if i>='a' and i<='z':
        print(chr((ord(i)-ord('a')+3)%26+ord('a')),end='')
    elif i>='A' and i<='Z':
        print(chr((ord(i)-ord('A')+3)%26+ord('A')),end='')
    else:
        print(i,end='')