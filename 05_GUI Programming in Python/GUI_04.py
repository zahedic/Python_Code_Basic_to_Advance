from tkinter import *
master = Tk()

#Create Label
Label(master,text='Name: ').grid(row=0)
Label(master,text='Father Name: ').grid(row=1)
Label(master,text='Mother Name: ').grid(row=2)

e1= Entry(master)
e2= Entry(master)
e3= Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
mainloop()

