import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ================= Database Setup =================
conn = sqlite3.connect("Library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL
)
""")
conn.commit()

# ================= Functions =================

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    try:
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Price must be a number")
        return

    if title == "" or author == "":
        messagebox.showerror("Error", "Title and Author required")
        return

    cursor.execute("INSERT INTO Books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
    conn.commit()
    messagebox.showinfo("Success", "Book added successfully!")
    clear_entries()
    view_books()

def view_books():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM Books")
    for book in cursor.fetchall():
        tree.insert("", tk.END, values=book)

def update_book():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select a book to update")
        return
    book_id = tree.item(selected_item[0])['values'][0]
    title = title_entry.get()
    author = author_entry.get()
    price_input = price_entry.get()
    price = float(price_input) if price_input else None

    if title:
        cursor.execute("UPDATE Books SET title = ? WHERE id = ?", (title, book_id))
    if author:
        cursor.execute("UPDATE Books SET author = ? WHERE id = ?", (author, book_id))
    if price is not None:
        cursor.execute("UPDATE Books SET price = ? WHERE id = ?", (price, book_id))
    conn.commit()
    messagebox.showinfo("Success", "Book updated successfully!")
    clear_entries()
    view_books()

def delete_book():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select a book to delete")
        return
    book_id = tree.item(selected_item[0])['values'][0]
    cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    conn.commit()
    messagebox.showinfo("Success", "Book deleted successfully!")
    view_books()

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        book = tree.item(selected_item[0])['values']
        title_entry.delete(0, tk.END)
        title_entry.insert(0, book[1])
        author_entry.delete(0, tk.END)
        author_entry.insert(0, book[2])
        price_entry.delete(0, tk.END)
        price_entry.insert(0, book[3])

# ================= GUI Setup =================
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")

# Labels and Entries
tk.Label(root, text="Title:").place(x=20, y=20)
title_entry = tk.Entry(root)
title_entry.place(x=100, y=20)

tk.Label(root, text="Author:").place(x=20, y=60)
author_entry = tk.Entry(root)
author_entry.place(x=100, y=60)

tk.Label(root, text="Price:").place(x=20, y=100)
price_entry = tk.Entry(root)
price_entry.place(x=100, y=100)

# Buttons
tk.Button(root, text="Add Book", command=add_book, width=15).place(x=350, y=20)
tk.Button(root, text="Update Book", command=update_book, width=15).place(x=350, y=60)
tk.Button(root, text="Delete Book", command=delete_book, width=15).place(x=350, y=100)
tk.Button(root, text="Clear Fields", command=clear_entries, width=15).place(x=350, y=140)

# Treeview for Display
tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Price"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Price", text="Price")
tree.place(x=20, y=200, width=550, height=180)
tree.bind("<<TreeviewSelect>>", on_tree_select)

view_books()  # Initially populate the tree

root.mainloop()
conn.close()
