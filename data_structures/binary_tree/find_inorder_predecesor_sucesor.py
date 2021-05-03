class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def findPredecessor(root):
    if(root.left != None): return findPredecessor(root.left)
    if(root.right != None): return findPredecessor(root.right)
    else: return root.data

def findSucessor(root):
    if root != None:
       findSucessor(root.left)
       findSucessor(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

#    4
#    /\
#   2  6
#  /\  /\
# 1  3 5 7

print(findPredecessor(root)) # 3
# print(findSucessor(root))    # 5