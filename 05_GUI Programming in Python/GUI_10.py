from tkinter import *
from tkinter import filedialog, messagebox, font
import os

root = Tk()
root.title("Professional Text Editor")
root.geometry("800x600")

# ---------------- Text Area ----------------
text_area = Text(root, wrap='word', undo=True, font=("Arial", 14))
text_area.pack(expand=True, fill='both')

# Keep track of current file
current_file = None

# ---------------- Functions ----------------
def new_file():
    global current_file
    if messagebox.askyesno("Confirm", "Do you want to create a new file? Unsaved changes will be lost."):
        text_area.delete(1.0, END)
        current_file = None
        root.title("New File - Text Editor")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, END)
        with open(file_path, "r", encoding="utf-8") as f:
            text_area.insert(END, f.read())
        current_file = file_path
        root.title(os.path.basename(file_path) + " - Text Editor")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, END))
        messagebox.showinfo("Saved", "File saved successfully!")
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, END))
        current_file = file_path
        root.title(os.path.basename(file_path) + " - Text Editor")
        messagebox.showinfo("Saved As", "File saved successfully!")

def print_file():
    messagebox.showinfo("Print", "Printing feature is under development!")

def exit_editor():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.quit()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def undo_action():
    try:
        text_area.edit_undo()
    except:
        pass

def redo_action():
    try:
        text_area.edit_redo()
    except:
        pass

# ---------- Text Styling ----------
def bold_text():
    current_tags = text_area.tag_names("sel.first")
    if "bold" in current_tags:
        text_area.tag_remove("bold", "sel.first", "sel.last")
    else:
        bold_font = font.Font(text_area, text_area.cget("font"))
        bold_font.configure(weight="bold")
        text_area.tag_configure("bold", font=bold_font)
        text_area.tag_add("bold", "sel.first", "sel.last")

def italic_text():
    current_tags = text_area.tag_names("sel.first")
    if "italic" in current_tags:
        text_area.tag_remove("italic", "sel.first", "sel.last")
    else:
        italic_font = font.Font(text_area, text_area.cget("font"))
        italic_font.configure(slant="italic")
        text_area.tag_configure("italic", font=italic_font)
        text_area.tag_add("italic", "sel.first", "sel.last")

def underline_text():
    current_tags = text_area.tag_names("sel.first")
    if "underline" in current_tags:
        text_area.tag_remove("underline", "sel.first", "sel.last")
    else:
        underline_font = font.Font(text_area, text_area.cget("font"))
        underline_font.configure(underline=True)
        text_area.tag_configure("underline", font=underline_font)
        text_area.tag_add("underline", "sel.first", "sel.last")

# ---------------- Menu Bar ----------------
menu_bar = Menu(root)
root.config(menu=menu_bar)

# ---------------- File Menu ----------------

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Print", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)


# ---------------- Edit Menu ----------------
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)


# ---------------- View Menu ----------------
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Bold", command=bold_text)
view_menu.add_command(label="Italic", command=italic_text)
view_menu.add_command(label="Underline", command=underline_text)

# ---------------- Scrollbar ----------------
scroll = Scrollbar(text_area)
scroll.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)

root.mainloop()
