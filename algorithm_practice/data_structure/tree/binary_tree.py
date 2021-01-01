# binary tree
# each parent has 2 children
# perfect : all leaves are full -- efficient (# of total node doubles every level)
# full : parent has 2 nodes

# # of nodes : level 0 : 2^0 = 1
# level 1: 2^1 = 2
# total = 2^h - 1
# log #nodes = height => log(n)

# binary search tree (ordered, flexible size)
# lookup,insert,delete O(log n) >< no O(1)
# balance is the key. Unbalanced ==> O(n)

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
  
  def remove(self, value):
    cur_node = self.root
    parent_node = None
    while (cur_node):
      if value < cur_node.value:
        parent_node = cur_node
        cur_node = cur_node.left

      elif value > cur_node.value:
        parent_node = cur_node
        cur_node = cur_node.right

      elif cur_node.value == value:
        
        if cur_node.right == None: # no right child
          if parent_node == None:
            self.root = cur_node.left
          else:
            if cur_node.value < parent_node.value:
              parent_node.left = cur_node.left
            elif cur_node.value > parent_node.value:
              parent_node.right = cur_node.left

        elif cur_node.right.left == None: # right child with no left child
          cur_node.right.left = cur_node.left
          if parent_node == None:
            self.root = cur_node.right
          else:
            if cur_node.value < parent_node.value:
              parent_node.left = cur_node.right
            elif cur_node.value > parent_node.value:
              parent_node.right = cur_node.right
        
        else:
          # find the right child's left most child
          leftmost = cur_node.right.left
          leftmost_parent = cur_node.right
          while (leftmost.left != None):
            leftmost_parent = leftmost
            leftmost = leftmost.left
          
          leftmost_parent.left = leftmost.right
          leftmost.left = cur_node.left
          leftmost.right = cur_node.right

          if parent_node == None:
            self.root = leftmost
          else:
            if cur_node.value < parent_node.value:
              parent_node.left = leftmost
            elif cur_node.value > parent_node.value:
              parent_node.right = leftmost  
        return
  
  def print_tree(self):
    if self.root != None:
      self.printt(self.root)

  def printt(self, curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.value))
      self.printt(curr_node.right)


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

tree.remove(1)
tree.print_tree()
