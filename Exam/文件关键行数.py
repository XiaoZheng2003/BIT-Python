ls=open("latex.log","r").readlines()
c=len(set(ls))
print("共{}关键行".format(c))