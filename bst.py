class BST:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

    def insert(self, n):
        if n < self.n: # passed-in n less than inherited n
            if self.left == None:
                self.left = BST(n) # don't understand why the passed-in n wouldn't be to the RIGHT
            else:
                self.left.insert(n) # recursive
        else:
            if self.right is None:
                self.right = BST(n)
            else:
                self.right.insert(n)
        return self

    def contains(self, n):
        """Accepts an integer; n is what we're looking for in the BST"""
        if n < self.n: # if passed-in n < current n
            if self.left is None:
                return False
            else:
                return self.left.contains(n) # recursive
        elif n > self.n:
            if self.right is None:
                return False
            else:
                return self.right.contains(n) # recursive
        else:
            return True

    def getMinN(self):
        if self.left is None:
            return self.n
        else:
            return self.left.getMinN() # recursive

    def getMaxN(self):
        if self.right is None: # base case
            return self.n
        else:
            return self.right.getMaxN() # recursive

    def remove(self, n, parent=None):
        if n < self.n:
            if self.left:
                self.left.remove(n, self)
        elif n > self.n:
            if self.right:
                self.right.remove(n, self)
        else:
            if self.left and self.right:
                self.n = self.right.getMinN()
                self.right.remove(self.n, self)
            elif parent is None:
                if self.left:
                    self.n = self.left.n
                    self.left = self.left.left
                elif self.right:
                    self.n = self.right.n
                    self.left = self.right.right
                    self.right = self.right.right
                else:
                    self.n = None

            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
        return self

bst_example = BST(39)
bst_example.insert(40)
bst_example.insert(50)
print(bst_example.getMinN())
print(bst_example.getMaxN())
bst_example.remove(50)
print(bst_example.getMaxN())





