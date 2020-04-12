"""
Quick and Dirty Binary Tree

Author:                 Felix Mark.
Date of modification:   11.04.2020
"""




# Imports
from enum import Enum




# Enum for Node positions
class Position(Enum):
    NONE =      0
    LEFT =      1
    RIGHT =     2
    
    

# Node class
class Node:
    """
    Node used to build a tree.
    """

    # Constructor
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.count = 1

    # Add a new node to self
    def add(self, node):
        if node.value < self.value:
            if self.left == None:   self.left = node
            else:                   self.left.add(node)
        elif not(node.value <= self.value):
            if self.right == None:  self.right = node
            else:                   self.right.add(node)
        else:
            self.count += 1
            
    # Remove value
    def remove(self, parent, isLeftChild, value, allOfThem = False):
        if self.value == value:
            if allOfThem or self.count <= 1:
                if self.left == None and self.right == None:
                    if isLeftChild: parent.left = None
                    else:           parent.right = None
                
                elif self.left == None and self.right != None:
                    if isLeftChild: parent.left = self.right
                    else:           parent.right = self.right
                
                elif self.right == None and self.left != None:
                    if isLeftChild: parent.left = self.left
                    else:           parent.right = self.left
                
                elif self.left != None and self.right != None:
                    cutie = self.right._findSmallestNode()
                    self.right.remove(self, False, cutie.value, allOfThem)
                    cutie.left = self.left
                    cutie.right = self.right
                    if isLeftChild: parent.left = cutie
                    else:           parent.right = cutie
            
            else:
                self.count -= 1
            
            return True
            
        else:
            if value < self.value and self.left != None:
                return self.left.remove(self, True, value, allOfThem)
            elif not(value <= self.value) and self.right != None:
                return self.right.remove(self, False, value, allOfThem)
            else:
                return False
        
    
    # Find smallest node
    def _findSmallestNode(self):
        return self if self.left == None else self.left._findSmallestNode()
    
    # Find value
    def find(self, value):
        if value < self.value and self.left != None:            return self.left.find(value)
        elif not(value <= self.value) and self.right != None:   return self.right.find(value)
        elif value == self.value:                               return True
        else:                                                   return False

    # Print the tree recursively
    def show(self, position, flat = False, depth = 0):
        # LEFT
        if self.left != None:   self.left.show(Position.LEFT, flat, depth+1)

        # SELF
        if flat == False:
            for i in range(0, depth):           print("\t", end='')
            if position == Position.NONE:       print("o", end=' ')
            elif position == Position.LEFT:     print("/", end=' ')
            elif position == Position.RIGHT:    print("\\", end=' ')
            else:                               print("ERROR: Position of Node is neither LEFT, RIGHT or NONE!!!")
        
        if not flat:
            print(self.value, end='')
            print("|"+str(self.count), end=' ')
        else:
            for i in range(0, self.count):
                print(self.value, end='')
                print(" ", end='')
            
        if not flat:
            if self.left != None and self.right != None:    print("<")
            elif self.left != None:                         print("/")
            elif self.right != None:                        print("\\")
            else:                                           print()

        # RIGHT
        if self.right != None:  self.right.show(Position.RIGHT, flat, depth+1)


        

# Tree class
class Tree:
    """
    Handles the root Node and manages the operations of the Nodes.
    """
    
    def __init__(self):
        self.root = None
    
    # Add a list of values
    def addAll(self, values):
        if isinstance(values, list):
            for value in values:    self.add(value)
        else:
            print("ERROR: The addAll function requires a list.")
    
    # Add a value
    def add(self, value):
        if self.root == None:       self.root = Node(value)
        else:                       self.root.add(Node(value))
    
    # Remove a list of values
    def removeAll(self, values):
        returnValue = True
        if isinstance(values, list):
            for value in values:    returnValue &= self.remove(value)
        else:
            print("ERROR: The removeAll function requires a list.")
        return returnValue
    
    # Remove a value
    def remove(self, value, allOfThem = False):
        if self.root == None:
            print("Tree empty.")
            return False
        else:
            if self.root.value == value:
                if allOfThem or self.root.count <= 1:
                    if self.root.left == None and self.root.right == None:
                        self.root = None
                    
                    elif self.root.left == None and self.root.right != None:
                        self.root = self.root.right
                    
                    elif self.root.right == None and self.root.left != None:
                        self.root = self.root.left
                    
                    elif self.root.left != None and self.root.right != None:
                        cutie = self.root.right._findSmallestNode()
                        self.root.right.remove(self.root, False, cutie.value, allOfThem)
                        cutie.left = self.root.left
                        cutie.right = self.root.right
                        self.root = cutie
                
                else:
                    self.root.count -= 1
                
                return True
                
            else:
                if value < self.root.value and self.root.left != None:
                    return self.root.left.remove(self.root, True, value, allOfThem)
                elif not(value <= self.root.value) and self.root.right != None:
                    return self.root.right.remove(self.root, False, value, allOfThem)
                else:
                    return False
                
                
        
    # Find a value
    def find(self, value):
        if self.root == None:
            print("Tree empty.")
            return False
        else:
            return self.root.find(value)
            
    # Print the tree
    def show(self, flat = False):
        if self.root == None:
            print("Tree empty.")
        else:
            if flat == True:    print("Flat:", end=' ')
            self.root.show(Position.NONE, flat)
            if flat == True:    print()







            
            
def main():
    """
    A quick and dirty test if the basic functionality is given.
    """
    
    print("Tree is executed as MAIN. Testing functionality.")
    
    # Create a tree in a garden dictionary and test stuff
    tree = Tree()
    tree.add(5)
    tree.addAll([10,2,4,7,1,8,3,3,3,3,9,2,0,12])
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
    if tree.remove(3,True):         print("PASS: Removed all 3.")
    else:                           print("ERROR: Could not remove all 3.")
    if tree.removeAll([12,2,4]):    print("PASS: Removed 12, 2 and 4.")
    else:                           print("ERROR: Could not remove 12, 2 and 4.")
    if not tree.remove(3):          print("PASS: Could not remove 3.")
    else:                           print("ERROR: Could remove 3.")
    tree.add(5)
    print();
    tree.show()
    print()
    tree.show(True)
    print()
    
    
    

# If script is called as main
if __name__ == "__main__":
    main()
