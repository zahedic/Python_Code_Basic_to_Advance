#Import Module
from tkinter import *
# Create root window
root=Tk()
#Root Window title and dimension
root.title('WELCOME TO ICON COMPUTER TECHNOLOGY')
#Set Geometry(width x height)
root.geometry('1000x800')

# Adding menu bar in root window
# New item in menu bar labelled as 'New'
# Adding more item in the menu bar

menu=Menu(root)
item=Menu(menu)
item.add_command(label='New')
item.add_cascade(label='File',menu=item)
root.config(menu=menu)

# Adding a label to the root window
lb1=Label(root,text="Write Your Name: ")
lb1.grid()

#Adding Entry Field
txt=Entry(root,width=10)
txt.grid(column=1,row=0)


#function to display text when
# button is cli
def clicked():
    res='My Name is '+ txt.get()
    lb1.configure(text=res)

#Button widget with red color text
#inside
btn=Button(root,text='Click me', fg='red', command=clicked)

#Set Button Grid
btn.grid(column=2,row=0)

#all widgets will be here
# Execute Tkinter
root.mainloop()

