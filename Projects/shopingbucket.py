print("\t======FOOD BUCKET======")
b=[]
a=int(input("Enter how many customer :"))

def intro():
    for i in range(a):
        d=input('Enter cusomer name :')
        b.append(d)

def name():
    for i in b:
        print("Hello ",i)
    print(":PLEASE SELECT YOUR ITEM:")

def item(f,x):
    print(f"You have purchase {f[0]}",x)



if __name__=="__main__":
    intro()
    name()
    print("1 BURGER rs 150\n2 PIZZA rs 300\n3 FRENCH FRIES rs 250\n4 MOMO rs 100")
    itm=["burger","pizza","frech fries","momo"]
    n=input("Enter the item :")
    item(itm,n)
    