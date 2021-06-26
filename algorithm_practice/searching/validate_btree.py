# https://leetcode.com/problems/validate-binary-search-tree/

# left key smaller then parent's key
# right key greater than parent's key
# input as list [2, 1, 3]


class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

  def isValidBST(self, root) -> bool:
    queue = [root]

    while(len(queue)>0):
      cur_node = queue[0]
      del queue[0]

      if cur_node.left != None:
        if cur_node.left.val >= cur_node.val:
          return False
        else:
          queue.append(cur_node.left)
      if cur_node.right != None:
        if cur_node.right.val <= cur_node.val:
          return False
        else:
          queue.append(cur_node.right)
    return True
    

btree = TreeNode(2, TreeNode(1), TreeNode(3))
print(btree.isValidBST(btree))

btree2 = TreeNode(5, TreeNode(1, None, None), TreeNode(4, 3, 6))
print(btree2.isValidBST(btree2))

btree3 = TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3, None, None), TreeNode(7, None, None)))
print(btree3.isValidBST(btree3))