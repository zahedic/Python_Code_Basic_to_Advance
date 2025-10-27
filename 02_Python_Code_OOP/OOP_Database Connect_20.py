# --------------------- Import Database ---------------------
import sqlite3

# --------------------- Database connect ---------------------
conn = sqlite3.connect("Library.db")
cursor = conn.cursor()

# --------------------- Create Table ---------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL
)
""")
conn.commit()


# --------------------- Functions for CRUD operations ---------------------

# --------------------- Insert Book ---------------------
def add_book(title, author, price):
    cursor.execute("INSERT INTO Books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
    conn.commit()
    print("Book added successfully!")


# --------------------- Fetch All Books ---------------------
def view_books():
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    for book in books:
        print(book)


# --------------------- Update Book ---------------------
def update_book(book_id, title=None, author=None, price=None):
    if title:
        cursor.execute("UPDATE Books SET title = ? WHERE id = ?", (title, book_id))
    if author:
        cursor.execute("UPDATE Books SET author = ? WHERE id = ?", (author, book_id))
    if price:
        cursor.execute("UPDATE Books SET price = ? WHERE id = ?", (price, book_id))
    conn.commit()
    print("Book updated successfully!")


# --------------------- Delete Book ---------------------
def delete_book(book_id):
    cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    conn.commit()
    print("Book deleted successfully!")


# ---------------------  Menu-driven program ---------------------
while True:
    print("\n==== Library Menu ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        price = float(input("Price: "))
        add_book(title, author, price)

    elif choice == "2":
        view_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID to update: "))
        title = input("New Title (leave blank if not change): ")
        author = input("New Author (leave blank if not change): ")
        price_input = input("New Price (leave blank if not change): ")
        price = float(price_input) if price_input else None
        update_book(book_id, title or None, author or None, price)

    elif choice == "4":
        book_id = int(input("Enter Book ID to delete: "))
        delete_book(book_id)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

# ---------------------  Close connection ---------------------
conn.close()
