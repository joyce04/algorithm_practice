# DFS [9, 4, 20, 1, 6, 15, 170] : memory = height of the tree
#    9
#  4    20
# 1 6  15 170

# in order [1, 4, 6, 9, 15, 20, 170]
# pre order [9, 4, 1, 6, 20, 15, 170] -- root에서 부터
# post order [1, 6, 4, 15, 170, 20, 9]

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
  
  def traverse_inorder(self, node, n_list):
    if (node.left):
      self.traverse_inorder(node.left, n_list)
    # base case
    n_list.append(node.value)

    if (node.right):
      self.traverse_inorder(node.right, n_list)
    return list
  
  def traverse_preorder(self, node, n_list):
    # base case
    n_list.append(node.value)
    if (node.left):
      self.traverse_preorder(node.left, n_list)
    if (node.right):
      self.traverse_preorder(node.right, n_list)
    return list
  
  def traverse_postorder(self, node, n_list):
    if (node.left):
      self.traverse_postorder(node.left, n_list)
    if (node.right):
      self.traverse_postorder(node.right, n_list)
    # base case
    n_list.append(node.value)
    return list

  def dfs_inorder(self):  #left child - parent - right childe : lowest number to largest
    queue = deque()
    self.traverse_inorder(self.root, queue)
    print(queue)

  def dfs_preorder(self): #parent - left -right
    queue = deque()
    self.traverse_preorder(self.root, queue)
    print(queue)
  
  def dfs_postorder(self): #left - right - parent
    queue = deque()
    self.traverse_postorder(self.root, queue)
    print(queue)

    

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print_tree()

tree.dfs_inorder()
tree.dfs_preorder()
tree.dfs_postorder()

