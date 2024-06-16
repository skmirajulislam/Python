import matplotlib.pyplot as plt 
import numpy as np

'''todo uses for highligheted comment'''

#TODO:plot 1
plt.subplot(2,3,1)
y=np.array([70,79,68,90,59,65])
x=np.array(['chen-i','Mum-i','Del','bng-e','hy-bad','Noida'])
plt.grid(axis='y',color='green')
plt.title("Machine - learning")
plt.xlabel("City")
plt.ylabel("Salary - LPA")
plt.bar(x,y,color='hotpink')


#TODO:plot 2
plt.subplot(2,3,3)
plt.title("Machine - learning")
x=np.array([2006,2008,2010,2014,2018,2023,2026])
y=np.array([2,3,4,8,10,12,16])
y1 = np.array([3, 8, 1, 10])
plt.grid(axis='y',color='blue')
plt.xlabel("Year")
plt.ylabel("Rate")
plt.plot(x,y,marker = 'o')


#plot 4
plt.subplot(2,3,6)
y = np.array([40, 25, 25, 10])
mylabels = ["ML engineer", "Software Developer", "Full stack Developer", "UX-Ui designer"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.xlabel("Feature Selection Tcm")
plt.legend(title = "Data in range")


#plot 5
plt.subplot(2,3,4)
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.ylabel("Data overfitting ML")
plt.xlabel("Princaple of Component Analylis P1")
plt.grid()
plt.scatter(x, y)


plt.show()

