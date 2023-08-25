import os
import sys


def fileread(n):
    f = open(n, "r")
    print("\nFILE DATA IS :", f.read())
    f.close()


def writefile(n):
    f = open(n, "w")
    print("Opps purivous part not exist...!\n")
    l = input("ENTER NEW DATA : ")
    f.write(l)
    f.close()


def appendf(n):
    f = open(n, "a")
    y = input("ENTER DATA : ")
    f.write(y)
    f.close()
    f = open(n, "r")
    print(f.read())


def delete(n):
    print(f"\nFILE DELETED {n}")
    os.remove(n)


def new(n):
    f = open(n, "x")
    c = input("ENTER NEW DATA : ")
    f.write(c)
    f.close()
    f = open(n, "r")
    print("\nNEW DATA IS :", f.read())
    print("\nNEW FILE CREATED PLEASE CONTINUE ")


if __name__ == "__main__":

    a = input("Enter a path : ")

    if os.path.exists(a):

        print("-.-.-.-: FILE EXIST :-.-.-.-")
        b = 1

        while b > 0:
            print("\n1 FOR READ FILE\n2 FOR WRITE FILE\n3 FOR APPEND\n4 FOR DELETE FILE")
            print("5 FOR END OPERATION")
            x = int(input("ENTER THE OPERATION :"))
            if os.path.exists(a):
                if x == 1:
                    fileread(a)

                elif x == 2:
                    writefile(a)

                elif x == 3:
                    appendf(a)

                elif x == 4:
                    delete(a)

                elif x == 5:
                    sys.exit("\nOPERATION ENDED")

            elif x== 5:
                    sys.exit("\nOPERATION ENDED")

            else:
                print("CREATING NEW FILE FOR JOB")
                print(f"NEW FILE PATH IS :{a}")
                new(a)

    else:

        print("---- FILE NOT EXIST ----\n")
        print("-: CREATE NEW FILE :-")
        b = 1

        while b > 0:
            print("\n1 FOR READ FILE\n2 FOR WRITE FILE\n3 FOR APPEND\n4 FOR DELETE FILE")
            print("5 FOR END OPERATION")
            x = int(input("ENTER THE OPERATION :"))
            if os.path.exists(a):
                if x == 1:
                    fileread(a)

                elif x == 2:
                    writefile(a)

                elif x == 3:
                    appendf(a)

                elif x == 4:
                    delete(a)

                elif x == 5:
                    sys.exit("\nOPERATION ENDED")

            elif x==5:
                sys.exit("\nOPERATION ENDED")

            else:
                print("CREATING NEW FILE FOR JOB ")
                print(f"NEW FILE PATH IS :{a}")
                new(a)

# C:\Users\Sk Miraj\OneDrive\Pictures\Documents
# "C:\Users\Sk Miraj\OneDrive\Pictures\Documents\software.txt"
# this software devloped by sk miraj
