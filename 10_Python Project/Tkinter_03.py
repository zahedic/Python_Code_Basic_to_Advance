#Import Module
from tkinter import *
# Create root window
root=Tk()
#Root Window title and dimension
root.title('WELCOME TO ICON COMPUTER TECHNOLOGY')
#Set Geometry(width x height)
root.geometry('1000x800')

# Adding a label to the root window
lb1=Label(root,text="What is Your Name?")
lb1.grid()

#function to display text when
# button is cli
def clicked():
    lb1.configure(text="My Name is Zahedul Islam Chowdhury")

#Button widget with red color text
#inside
btn=Button(root,text='Click me', fg='red', command=clicked)

#Set Button Grid
btn.grid(column=1,row=0)

#all widgets will be here
# Execute Tkinter
root.mainloop()

