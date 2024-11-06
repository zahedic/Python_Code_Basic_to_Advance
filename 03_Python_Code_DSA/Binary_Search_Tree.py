class Student:
    def __init__(self,sid,name,gpa):
        self.sid=sid
        self.name=name
        self.gpa=gpa

    def __repr__(self):
        return f"SID:{self.sid}, Name: {self.name} GPA: {self.gpa} "

class Binary_Search_Tree:
    def __init__(self,key,value):
        self.key=key
        self.value = value
        self.left_child=None
        self.right_child=None

    def insert(self,key,value):
        if key < self.key:
            if self.left_child:
                self.left_child.insert(key,value)
            else:
                self.left_child=Binary_Search_Tree(key,value)

        elif key>self.key:
            if self.right_child:
                self.right_child.insert(key,value)
            else:
                self.right_child=Binary_Search_Tree(key,value)

        else:
            print('This ID already exits.')

    def search(self,key):
        if self.key==key:
            return self.value

        elif key<self.key:
            if self.left_child:
                return self.left_child.search(key)
            else:
                return None
        else:
            if self.right_child:
                return self.right_child.search(key)
            else:
                return None

    def inorder_traversal(self):
        if self.left_child:
            self.left_child.inorder_traversal()

        print(self.value)

        if self.right_child:
            self.right_child.inorder_traversal()



Students=[
    Student(101,"Zawad Islam",5.00),
    Student(102,"Awad Islam",5.00),
    Student(103,"Mahin",5.00)
]


root=Binary_Search_Tree(Students[0].sid,Students[0])

for Student in Students[1:]:
    root.insert(Student.sid,Student)

#print("In Order Traversal :")
#root.inorder_traversal()

search_id=int(input('Enter Your SID: '))
result=root.search(search_id)

if result:
    print(f"\n Congratulation {result}")
else:
    print(f"\n This ID {search_id} is not found")























