from tkinter import *
root=Tk()

#Create RadioButton
var1=IntVar()
Radiobutton(root, text='Male', variable=var1, value=1).pack(anchor=W)
Radiobutton(root, text='Female', variable=var1, value=2).pack(anchor=W)

mainloop()

