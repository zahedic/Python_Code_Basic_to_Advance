from tkinter import *
from tkinter import filedialog,messagebox,font
import os

root=Tk()
root.title('Text Editor++')
root.geometry('800x600')


#-----------------------Text Area-----------------------
text_area= Text(root,wrap='word', undo=True, font=('Arial',14))
text_area.pack(expand=True, fill='both')

#-----------------------Current File-----------------------
current_file=None

#-----------------------Functions-----------------------


def save_file():
    global current_file
    if current_file:
        with open(current_file,'w',encoding='utf-8') as f:
            f.write(text_area.get(1.0,END))
        messagebox.showinfo('Save','File Save Successfully! ')
    else:
        save_as_file()



def save_as_file():
    global current_file
    file_path=filedialog.asksavesfilename(defaultexttension='.txt',filetypes=[('Text Files','*.txt'),('All Files','*.*')])

    if file_path:
        with open(file_path,'w',encoding='utf-8') as f:
            f.write(text_area.get(1.0,END))
        current_file=file_path
        root.title(os.path.basename(file_path)+'- Text Editor')
        messagebox.showinfo('Save As','File Save Successfully!')

def bold_text():
    current_tags=text_area.tag_names('sel.first')
    if 'blod' in current_tags:
        text_area.tag_remove('bold','sel.first','sel.last')
    else:
        bold_font=font.Font(text_area,text_area.cget('font'))
        bold_font.configure()


#-----------------------Menu Bar -----------------------
menu_bar=Menu(root)
root.config(menu=menu_bar)


#-----------------------File Menu -----------------------
file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save',command=save_file)
file_menu.add_command(label='Save As')
file_menu.add_command(label='Print')
file_menu.add_separator()
file_menu.add_command(label='Exit')


#-----------------------Edit Menu -----------------------
edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')

#-----------------------View Menu -----------------------
view_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='View',menu=view_menu)
view_menu.add_command(label='Bold',command='bold_text')
view_menu.add_command(label='Italic')
view_menu.add_command(label='Underline')



root.mainloop()