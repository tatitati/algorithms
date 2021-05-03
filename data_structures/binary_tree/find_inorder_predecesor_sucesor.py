class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print(root.data)
       inOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#    1
#    /\
#   2  3
#  /\
# 4  5

print(inOrder(root))   # 4 2 5 1 3