books=[]
books.append('Java')
books.append('Python')
books.append('C++')
books.append('C#')


print(books)
books.pop()
books.pop()
books.pop()
books.pop()
books.pop()

print(books)
if not books:
    print('No book here')