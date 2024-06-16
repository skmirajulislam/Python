import random
import re


def catch_pass(a):
    if not re.search("[A-Z]", a):
        return False
    elif not re.search("[a-z]", a):
        return False
    elif not re.search("[0-9]", a):
        return False
    elif not re.search("[_&#@$]", a):
        return False
    elif not len(a) > 12 and len(a) < 8:
        return False
    else:
        return True


def genarte():
    x = random.sample("ABCDEFGHIJKLMNOPQRSTWXYZ", 5)
    y = random.sample("abcdefghizklmnopqrstwxyz", 5)
    z = random.sample("0123456789", 5)
    w = random.sample("@#$&", 4)
    main = x+y+z+w
    final = ''.join(random.sample(main, 8))
    return final


if __name__ == '__main__':
    bucket = []
    x = input("Enter the password : ")
    if catch_pass(x):
        print("Strong password ")
    else:
        print("Weak password I make another for you :")
        print(genarte())
