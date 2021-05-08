from collections import deque

class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

root = Node(52)
root.left = Node(40)
root.left.left = Node(24)
root.left.left.right = Node(32)
root.right = Node(62)
root.right.left = Node(58)
root.right.right = Node(69)

#    52
#    /\
#   40 62
#  /    /\
# 24  58  69
#   \
#    32

def inOrder(node):
    if(node.left != None): inOrder(node.left)
    print(node.data)
    if(node.right != None): inOrder(node.right)
    

print(inOrder(root))   # 24 32 40 52 58 62 69




def preOrder(node):   
    print(node.data) 
    if(node.left != None):  preOrder(node.left)
    if(node.right != None): preOrder(node.right)

print(preOrder(root))  # 52 40 24 32 62 58 69




def postOrder(node):
    if(node.left != None): postOrder(node.left)
    if(node.right != None): postOrder(node.right)
    print(node.data) 

print(postOrder(root)) # 32 24 40 58 69 62 52



