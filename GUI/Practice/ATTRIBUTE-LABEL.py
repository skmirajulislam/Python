import tkinter as tk

root = tk.Tk()
root.title('Attributes of label')

textD = tk.Label(text='''scikit-learn (formerly scikits.learn and also known as sklearn) is a \n
free software machine learning library for the Python programming language.\n
It features various classification, regression and clustering algorithms \n
including support-vector machines,random forests, gradient boosting, \n
k-means and DBSCAN, and is designed to interoperate with the Python \n
numerical and scientific libraries NumPy and SciPy.\n
Scikit-learn is a NumFOCUS fiscally sponsored project.''',
bg='cyan',
fg='black',
padx=23,pady=40,
font=('Times New Roman',19,'bold'),
relief='sunken',
borderwidth=3)

# === Importent abel options === :-
#1. font=('Times New Roman',19,'bold')
#2. font='Times New Roman 19 bold'
#text = adds the text
#bd = background
#fg = foreground
#font = sets the font
#padx = x padding
#pady = y padding
#relief = border styling -> SUNKEN,RAISED,GROVE,RIDGE 
#borderwidth = set border width (int)

textD.pack()
root.mainloop()
