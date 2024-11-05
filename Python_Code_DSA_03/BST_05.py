class Student:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
    def __repr__(self):
        return f"ID: {self.student_id}, Name: {self.name}, GPA: {self.gpa}"
class BinarySearchTree:
    def __init__(self, key, value):
        self.key = key  # Student ID (primary key)
        self.value = value  # Student object
        self.left = None
        self.right = None
    def insert(self, key, value):
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = BinarySearchTree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = BinarySearchTree(key, value)
        else:
            print("Duplicate key! Student with this ID already exists.")

    def search(self, key):
        if self.key == key:
            return self.value
        elif key < self.key:
            if self.left:
                return self.left.search(key)
            else:
                return None
        else:
            if self.right:
                return self.right.search(key)
            else:
                return None

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

# Sample Data
students = [
    Student(102, "Alice", 3.8),
    Student(101, "Bob", 3.5),
    Student(103, "Charlie", 3.9)
]

# Create the root of the BST
root = BinarySearchTree(students[0].student_id, students[0])

# Insert other students into the BST
for student in students[1:]:
    root.insert(student.student_id, student)

# In-order Traversal (to display students sorted by ID)
print("In-order Traversal (Sorted by Student ID):")
root.inorder_traversal()

# Search for a specific student by ID
search_id = 103
result = root.search(search_id)
if result:
    print(f"\nStudent Found: {result}")
else:
    print(f"\nStudent with ID {search_id} not found.")
