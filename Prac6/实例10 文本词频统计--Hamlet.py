def getText():
    txt=open("hamlet.txt","r",encoding="utf-8").read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘’{|}~':
        txt=txt.replace(ch," ")
    return txt

hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word=items[i][0]
    print(word)