from tkinter import *
master = Tk()

#Create CheckButton
var1=IntVar()
Checkbutton(master,text='S.S.C',variable=var1).grid(row=0,sticky=W)

var2=IntVar()
Checkbutton(master,text='H.S.C',variable=var2).grid(row=1,sticky=W)

var3=IntVar()
Checkbutton(master,text='B.SC',variable=var3).grid(row=2,sticky=W)

var4=IntVar()
Checkbutton(master,text='M.SC',variable=var4).grid(row=3,sticky=W)

mainloop()