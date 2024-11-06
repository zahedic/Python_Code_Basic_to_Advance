class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        print(" " * level * 2 + self.data)
        for child in self.children:
            child.print_tree(level + 1)

# Tree গঠন
root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("MacBook"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("ThinkPad"))

mobile = TreeNode("Mobile")
mobile.add_child(TreeNode("iPhone"))
mobile.add_child(TreeNode("Samsung"))

root.add_child(laptop)
root.add_child(mobile)

# গাছ প্রিন্ট করা
root.print_tree()
