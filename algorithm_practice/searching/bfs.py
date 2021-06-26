# BFS

# binary tree
from collections import deque

class TreeNode:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    node = TreeNode(value, None, None)
    if self.root is None:
      self.root = node
    else:
      cur_node = self.root
      ch_node = None
      while(cur_node):
        ch_node = cur_node
        if value < cur_node.value:
          cur_node = cur_node.left
        else:
          cur_node = cur_node.right
      if value < ch_node.value:
        ch_node.left = node
      else:
        ch_node.right = node
  
  def lookup(self, value):
    cur_node = self.root
    while(cur_node):
      if cur_node.value == value:
        return cur_node
      elif value < cur_node.value:
        cur_node = cur_node.left
      else:
        cur_node = cur_node.right
    return False
  
  def print_tree(self):
    if self.root != None:
      self.printt(self.root)

  def printt(self, curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.value))
      self.printt(curr_node.right)

  def bfs_array(self):
    queue = [self.root]
    vals = []

    while(len(queue)>0):
      cur_node = queue[0]
      del queue[0]
      vals.append(cur_node.value)
      if cur_node.left != None:
        queue.append(cur_node.left)
      if cur_node.right != None:
        queue.append(cur_node.right)
    return vals
  
  def bfs_deque(self):
    queue = deque()
    queue.append(self.root)
    vals = []

    while(len(queue)>0):
      cur_node = queue.popleft()
      vals.append(cur_node.value)
      if cur_node.left != None:
        queue.append(cur_node.left)
      if cur_node.right != None:
        queue.append(cur_node.right)
    return vals

  def bfs_recursive(self, queue, vals):
    if len(queue)==0:
      return vals
    else:
      cur_node = queue.popleft()
      vals.append(cur_node.value)
      if cur_node.left != None:
        queue.append(cur_node.left)
      if cur_node.right != None:
        queue.append(cur_node.right)
      return self.bfs_recursive(queue, vals)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print_tree()
print(tree.lookup(6))
print(tree.lookup(15))

print(tree.bfs_array())
print(tree.bfs_deque())

q = deque()
q.append(tree.root)
print(tree.bfs_recursive(q, []))
