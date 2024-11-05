# Implement Binary Search Tree
# Lecture 43
class Binary_Search_Tree:
    def __init__(self,key):
        self.key=key
        self.left_child=None
        self.right_child=None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return

        if self.key>data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child=Binary_Search_Tree(data)

        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child=Binary_Search_Tree(data)

    def search(self,data):
        if self.key == data:
            print('Node is found.')
            return
        





root=Binary_Search_Tree(20)
print(root.key)
print(root.left_child)
print(root.insert(20))
