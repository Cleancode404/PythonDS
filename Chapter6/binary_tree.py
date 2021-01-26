class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.left_child = None

    def insertlfe(self, newnode):
        if self.left_child == None:
            self.left_child = BinaryTree(newnode)

        else:
            t = BinaryTree(newnode)
            t.left_child = self.left_child
            self.left_child = t
    

    def insertright(self, newnode):
        if self.right_child == None:
            self.right_child == BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.right_child = self.right_chjild
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.inset_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())