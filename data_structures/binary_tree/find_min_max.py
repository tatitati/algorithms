class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def findMin(root):
   if root:
       if root.left == None: return root.data
       else: return findMin(root.left)

def findMax(root):
   if root:
       if root.right == None: return root.data
       else: return findMax(root.right)



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

print(findMin(root))   # 1
print(findMax(root))   # 7