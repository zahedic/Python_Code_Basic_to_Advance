from tkinter import *
root=Tk()
menu=Menu(root)
root.config(menu=menu)

filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')
filemenu.add_command(label='Print')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

editmenu=Menu(menu)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

viewmenu=Menu(menu)
menu.add_cascade(label='View',menu=viewmenu)
viewmenu.add_command(label='Bold')
viewmenu.add_command(label='Italic')
viewmenu.add_command(label='Underline')


mainloop()