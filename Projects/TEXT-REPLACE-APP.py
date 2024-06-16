import re
a=input("Enter the string :")
b=input("Enter the surch text :")
x=re.search(b,a)
if x:
    c=input("Enter the text to replace :")
    f=a.replace(b,c)
    print(f)
else:
    print("not match")