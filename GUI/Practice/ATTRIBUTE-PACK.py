import tkinter as tk

#1. font=('Times New Roman',19,'bold')
#2. font='Times New Roman 19 bold'
#text = adds the text
#bd = background
#fg = foreground
#font = sets the font ('style',size,'type)
#padx = x padding
#pady = y padding
#relief = border styling -> SUNKEN,RAISED,GROVE,RIDGE 
#borderwidth = set border width (int)

var =  tk.Tk()

var.geometry("444x233")
var.title("My Gui")

title_label = tk.Label(text='''scikit-learn (formerly scikits.learn and also known as sklearn) is a \n
free software machine learning library for the Python programming language.\n
It features various classification, regression and clustering algorithms \n
including support-vector machines,random forests, gradient boosting, \n
k-means and DBSCAN, and is designed to interoperate with the Python \n
numerical and scientific libraries NumPy and SciPy.\n
Scikit-learn is a NumFOCUS fiscally sponsored project.''',
bg='cyan',
fg='black',
padx=23,pady=40,
font=('Courier New',16,'bold'),
relief='sunken',
borderwidth=3)

run = tk.Label(text="READY",bg='red',relief='raised')

title_label.pack(anchor='nw',fill='x',padx=350,pady=100)
run.pack(fill='y',anchor='sw',side='bottom',padx=100,pady=100)

# === Importent pack options === :-
#anchor = nw,se, all other diraction
#side = top,bottom,right,left
#fill = x , y , none , both cordunate strech the item
#pady = y cordinate padding
#padx = x cordinate padding


var.mainloop()