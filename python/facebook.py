# first question: traverse a binary tree and print nodes out layer by layer
def breadth_traverse(tree):
    if not tree:
        return
    if not tree.left and not tree.right:
        print(tree.data)
        return
    this_layer, queue = [], []
    this_layer.append(tree)
    while this_layer:
        while this_layer:
            current = this_layer.pop(0)
            print(str(current.data)),
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print
        this_layer = list(queue) 
        queue = []

class BinaryTree():
    def __init__(self, *args, **kwargs):
        if not args:
            self.data = None
            self.right = None
            self.left = None
            return
        data = args[0]
        if type(data) is int:
            self.data = data
            self.right = None
            self.left = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data
    
    def setData(self, value):
        self.data = value

    def insertRight(self, x):
        if self.right == None:
            self.right = BinaryTree(x)
        else:
            tree = BinaryTree(x)
            tree.right = self.right
            self.right = tree

    def insertLeft(self, x):
        if self.left == None:
            self.left = BinaryTree(x)
        else:
            tree = BinaryTree(x)
            tree.left = self.left
            self.left = tree

    def insert(self, x):
        if x < self.data:
            if self.left == None:
                self.insertLeft(x)
            else:
                self.left.insert(x)
        elif x > self.data:
            if self.right == None:
                self.insertRight(x)
            else:
                self.right.insert(x)

def printTree(tree):
    if tree != None:
        printTree(tree.left)
        print(tree.data)
        printTree(tree.right)

bloop = BinaryTree(6)

bloop.insert(4)
bloop.insert(8)

bloop.insert(2)
bloop.insert(5)

bloop.insert(7)
bloop.insert(9)

# output of breadth_traverse(bloop) should be:
# 6
# 4 8
# 2 5 7 9

# second question: given two binary strings, print sum of the strings in binary



# felix' first question: given a hash of the alphabet mapping letter to number i.e.
# {a:1, b:2, ..}, find all possible permutations of a translation from number to 
# word
# i.e. 103 -> 103 only, so 10, 3, so kc
