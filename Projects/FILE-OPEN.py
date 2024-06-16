f = open('Guitkinter\\software\\data.txt','+a')
f.write('Hello')
f.close()

f = open('Guitkinter\\software\\data.txt','r')
print(f.read())
f.close()