import random
import re

def  password(n):
    if not re.search("[a-z]",n):
        return False
    if not re.search("[A-Z]",n):
        return False
    if not re.search("[~!@#$%&^*()]",n):
        return False
    if not re.search("[0-9]",n):
        return False
    else :
        return True
    
def list_to_str(x):
    string=""
    for i in x:
        string+=i
    return string

def verifier(n):
    if n:
        print("Strong pass word ")
    else:
        print("Week password i try another one...")
        x=random.sample("13579xwqkzpyAKXWEQ@#$%^&*",8)
        print("your pass word is : ",x)
        word=list_to_str(x)
        print("AFTER CONVERSION : ",word)
        x=password(word)
        if x:
            print("strong password")
        else:
            verifier(x)

if __name__=='__main__':
    a=input("Enter the pass word : ")
    check=password(a)
    def convert(n):
        if n:
            print("Strong pass word ")
        else:
            print("Week password i can genarate strong one for you....")
            x=random.sample("13579xwqkzpyAKXWEQ@#$%^&*",16)
            print("your pass word is : ",x)
            word=list_to_str(x)
            print("AFTER CONVERSION : ",word)
            xen=password(word)
            verifier(xen)
    convert(check)

