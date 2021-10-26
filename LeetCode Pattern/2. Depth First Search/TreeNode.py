class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  ## a method to create a Tree from BFS array
  # it is similar to BFS traversal. We take care a layer and a pair of array items
  # and think about the properties in LeetCode examples that how to handle null
  def create(self, arr):
    if not arr:
      return None

    root = TreeNode(arr.pop(0))
    queue = [root]

    while arr:
      levelSize = len(queue)
      for i in range(levelSize):
        # in some time, arr will become empty if the last leaves have null value
        if not len(arr):
          break
        # except for root value, we pop out two elements each time
        left = arr.pop(0)
        right = arr.pop(0)
        # we pop out one node and link it to the left and right node
        node = queue.pop(0)
        # if no left and right children, this node is a leaf then we continue
        if left == None and right == None: 
          continue
        # otherwise, we append left or right child if one or both of them exist
        if left != None:
          node.left = TreeNode(left)
          queue.append(node.left)
        if right != None:
          node.right = TreeNode(right)
          queue.append(node.right)

    return root

  ## using template of BFS traversal to show all nodes in array
  def show (self):
    if not self:
      return None
    queue = [self]
    result = []
    while queue:
      crrLevelSize = len(queue)
      for i in range(crrLevelSize):
        node = queue.pop(0)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        result.append(node.val)  
    return result