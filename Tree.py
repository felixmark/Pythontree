"""
A Python Binary Tree

Tree does not store values added twice.

Author:                 Felix Mark.
Date of modification:   29.08.2020
"""




# ==================================== Node ====================================

class Node:
    """Node used to build a tree."""
    
    def __init__(self, value):
        """Constructor"""
        
        self.left = None
        self.right = None
        self.value = value

    def add(self, value):
        """Add a node. Smaller ones left, larger ones right and the same ones increase the counter."""
        
        if value == self.value:
            return False
        elif value < self.value:
            if self.left == None:
                self.left = Node(value)
                return True
            else:
                return self.left.add(value)
        elif value > self.value:
            if self.right == None:
                self.right = Node(value)
                return True
            else:
                return self.right.add(value)
    
    def remove(self, parent, isLeftChild, value):
        """Remove a node."""
        
        if value == self.value:
            if self.left == None and self.right == None:
                # No children. Make parent remove self.
                if isLeftChild: parent.left = None
                else:           parent.right = None
            
            elif self.left == None and self.right != None:
                # Got right child. Make parent append right child.
                if isLeftChild: parent.left = self.right
                else:           parent.right = self.right
            
            elif self.right == None and self.left != None:
                # Got left child. Make parent append left child.
                if isLeftChild:
                    parent.left = self.left
                else:
                    parent.right = self.left
            
            elif self.left != None and self.right != None and parent != None:
                # Got left and right child.
                child = self.right._findSmallestNode()
                self.right.remove(self, False, child.value)
                child.left = self.left
                child.right = self.right
                if isLeftChild:
                    parent.left = child
                else:
                    parent.right = child
            
            else:
                # Got left and right child and node is root.
                child = self.right._findSmallestNode()
                self.right.remove(self, False, child.value)
                self.value = child.value
            
            return True
            
        else:
            # Not the value to remove. Go deeper.
            if value < self.value and self.left != None:
                return self.left.remove(self, True, value)
            elif value > self.value and self.right != None:
                return self.right.remove(self, False, value)
            else:
                return False
        
    def _findSmallestNode(self):
        """Finds the smallest value."""
        
        return self if self.left == None else self.left._findSmallestNode()
    
    def find(self, value):
        """Finds a value."""
        
        if value == self.value:
            return True
        elif value < self.value and self.left != None:
            return self.left.find(value)
        elif value > self.value and self.right != None:
            return self.right.find(value)
        else:
            return False

    def show(self, nodetype_string, flat = False, depth = 0):
        """Print the tree recursively."""
        
        # LEFT
        if self.left != None:
            self.left.show("/", flat, depth+1)

        # SELF
        if not flat:
            for i in range(0, depth):
                print("\t", end='')
            print(nodetype_string, end=' ')
            print(self.value, end=' ')
            if self.left != None and self.right != None:
                print("<")
            elif self.left != None:
                print("/")
            elif self.right != None:
                print("\\")
            else:
                print()
        else:
            print(self.value, end=' ')

        # RIGHT
        if self.right != None:
            self.right.show("\\", flat, depth+1)


        


# ==================================== Tree ====================================

class Tree:
    """Handles the root Node and manages the operations of the Nodes."""
    
    def __init__(self):
        """Constructor"""
        
        self.root = None
    
    def add(self, value):
        """Add a value to the tree."""
        
        if self.root == None:
            self.root = Node(value)
            return True
        else:
            return self.root.add(value)
    
    def remove(self, value):
        """Remove a value from the tree."""
        
        return self.root.remove(None, True, value) if self.root is not None else False
        
    def find(self, value):
        """Find a value in the tree."""
        
        return self.root.find(value) if self.root is not None else False
            
    def show(self, flat = False):
        """Print the tree."""
        
        if self.root == None:
            return False
        
        if flat == True:    print("Flat:", end=' ')
        self.root.show("o", flat)
        if flat == True:    print()
        return True
    
    def addAll(self, values):
        """Add a list of values to the tree."""
        
        if not isinstance(values, list):
            raise TypeError("The addAll function requires a list.")
        
        returnValue = True
        for value in values:
            returnValue &= self.add(value)
        return returnValue
    
    
    def removeAll(self, values):
        """Remove a list of values from the tree."""
        
        if not isinstance(values, list):
            raise TypeError("The removeAll function requires a list.")
        
        returnValue = True
        for value in values:
            returnValue &= self.remove(value)
        return returnValue







            
            
def main():
    """A quick and dirty test if the basic functionality is given."""
    
    print("Tree is executed as main. Testing functionality.")
    
    # Create a tree in a garden dictionary and test stuff
    tree = Tree()
    tree.add(5)
    tree.addAll([10,2,4,7,8,1,8,3,3,3,3,9,2,0,12,20,18,27,6,-2,-5])
    tree.show()
    if tree.find(-1):               print("ERROR: Tree contains -1.")
    else:                           print("PASS: Tree does NOT contain -1.")
    if tree.find(1):                print("PASS: Tree contains 1.")
    else:                           print("ERROR: Tree does NOT contain 1.")
    if tree.remove(1):              print("PASS: Removed 1")
    else:                           print("ERROR: Did NOT remove 1.")
    if tree.remove(10):             print("PASS: Removed 10")
    else:                           print("ERROR: Did NOT remove 10.")
    if tree.find(1):                print("ERROR: Tree contains 1.")
    else:                           print("PASS: Tree does NOT contain 1.")
    if tree.find(10):               print("ERROR: Tree contains 10.")
    else:                           print("PASS: Tree does NOT contain 10.")
    if tree.remove(5):              print("PASS: Removed 5")
    else:                           print("ERROR: Did NOT remove 5.")
    if tree.remove(3):              print("PASS: Removed 3.")
    else:                           print("ERROR: Could not remove 3.")
    if tree.removeAll([12,2,4]):    print("PASS: Removed 12, 2 and 4.")
    else:                           print("ERROR: Could not remove 12, 2 and 4.")
    if not tree.remove(3):          print("PASS: Could not remove 3.")
    else:                           print("ERROR: Could remove 3.")
    if tree.remove(7):              print("PASS: Removed root.")
    else:                           print("ERROR: Could not remove root.")
    if not tree.add(9):             print("PASS: Tree could NOT add 9.")
    else:                           print("ERROR: Tree could add 9.")
    print();
    tree.show()
    print()
    tree.show(True)
    print()
    
    
    

# If script is called as main
if __name__ == "__main__":
    main()
