from collections import deque

class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
    if(root.left != None):inOrder(root.left)
    print(root.data)
    if(root.right != None):inOrder(root.right)

def preOrder(root):
   if root:
       print(root.data)
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print(root.data)

def levelOrder(root):
    if root is None: return
    
    queue = []    
    queue.append(root)
 
    while(len(queue) > 0):
        print (queue[0].data)
        node = queue.pop(0)
  
        if node.left is not None:  queue.append(node.left)
        if node.right is not None: queue.append(node.right)    

def levelOrderReverse(root): # leaves to root
    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:continue    
        ans.appendleft(node.data)
      
        if node.right: q.append(node.right)              
        if node.left:  q.append(node.left)
              
    return ans



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

print(inOrder(root))   # 24 32 40 52 58 62 69
print(preOrder(root))  # 52 40 24 32 62 58 69
print(postOrder(root)) # 32 24 40 58 69 62 52
print(levelOrder(root)) # 52 40 62 24 58 69 32
print(levelOrderReverse(root)) # 32 24 58 69 40 62 52