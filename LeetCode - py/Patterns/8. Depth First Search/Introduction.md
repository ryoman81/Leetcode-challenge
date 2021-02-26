# Pattern: Depth First Search, 深度优先搜索

起初准备这个类别时, 当作和BFS类似的练习方式, 先通过对树上的DFS一众操作的学习, 加深了解, 再扩展到其它高频的应用. 但经过一番探索之后, 感觉DFS下的问题框架很庞大, DFS更加抽象成一种操作思维, 从而延展到几乎 recursion, backtracking, 还有很多DP问题的基础思维都要用到DFS去处理. 因此, 这个章节应该是所有topic当中最为庞大和复杂的类型 (毕竟Leetcode上DFS tag就有四页, 超过两百道题目了~)

**!!做题顺序请务必按照本介绍当中顺序进行!!**

## **类别总结:**
同上一个BFS类似, 在第一轮的总结归纳中, 我们希望对基本的在树上的DFS操作进行第一轮总结学习. 而后, 需要细致总结backtracking回溯法问题, Recursion的基本规范, 以及广泛高频题 (迷宫, 二维矩阵, 岛等应用题)的总结学习.

### 1.1 树上的DFS遍历
树上的DFS绕不开基本的遍历方法, 参见reference #1以及之前面试课程当中的介绍, DFS traversal 包含了 post-order, pre-order, and in-order. 
<img src="https://upload-images.jianshu.io/upload_images/10107787-c8dc2e6b5c6044bd.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp" />

对应的伪码

```py
def preDFS (node):
  if not node:
    return
  result.append(node.val)
  preDFS(node.left)
  preDFS(node.right)
```

```py
def postDFS (node):
  if not node:
    return
  preDFS(node.left)
  preDFS(node.right)
  result.append(node.val)
```

```py
def inDFS (node):
  if not node:
    return
  preDFS(node.left)
  result.append(node.val)
  preDFS(node.right)
```

在pre-order 前序遍历方法中, 处理node的顺序是和访问节点顺序一致. 根据前序遍历出来的序列数组也是最容易还原出一颗二叉树结构. 

### 1.2 树上的DFS路径问题
掌握树上的BFS遍历之后, 进而下一类问题就是树上路径的遍历. 可以想象, 前者是遍历整棵树的节点进而保存下来, 而路径遍历后者是遍历树中所有可能的路径. 这类问题非常火, 诸如 Path Sum 的众多变种. 请参考:
ref: https://zhuanlan.zhihu.com/p/112370893 

根据做完的题目112, 113, 257, 129, 可以总结一个处理从根节点到叶节点, 遍历所有root-to-leaf的小模板
```py
def searchPath (root): 
  # define some varibles in outlayer scope of function (closure闭包)
  result =      # a result might be the number of path or something else
  path = []     # a list/array to store the path (if needed)

  # then we define a recursive function within this closure 
  # The reason is this function can get access to the closure variables
  def DFS (node):
    # base case of course, if node is null
    if not node:
      return
    
    # push in the current node to the path
    path.append(node.val)

    # a key step to check if the current node is leaf
    if not node.left and not node.right:
      # do some thing to update result or record this path. 
      if conditions:

      # Be careful with two things:
      # 1. In most languages, if we want to record path to the result, we need to make a hard copy
      #    Because the record of path is a reference. Its change will result in problems. 
      result.append(path.copy()) # or path[:]
      # 2. In Python, if we want to change closure variable 'result', we need to desclare 'nonlocal'
      nonlocal result
      result += 1

    # next we do recursion steps by left and right
    DFS(node.left)
    DFS(node.right)

    # Anytime we jump out from left and right, we should do backtracking (回溯)
    # In this path search problem, we need to pop out the current node
    path.pop()

    # then this code will return to its parent node
```

题目437和124是两种更难的path search问题, 因为寻找的路径不一定是root-to-leaf. 因此上面的模板不能够直接套用. 但可以根据相似的递归思路, 设计好闭包当中需要记录的变量, 和recursion函数. 例如437使用到的前缀和, 实际上和DP当中股票预测最低最高点那个问题很类似. 而124相对更为复杂, 路径不一定是root-to-leaf, 甚至不一定是downwards, 那么遍历时, 每个节点需要记录的信息又应该是别的东西. 

总结而言, 遍历路径的问题和上述的模板比较适配. 尽管该模板不是所有网上答案都用的形式, 以个人顺手形式为准.

### 1.3 DFS构建/还原二叉树
又是超级超级常见的类别, 题目要求常常是给定特殊的数组, 例如前/中/后序遍历的数组, 或者是排好序的数组或链表, 要求还原出原本的树或二叉搜索树. 这篇文章的详解十分到位可以做为参考: https://lucifer.ren/blog/2020/02/08/%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%93%E9%A2%98/



## **经典题目:**

### **Tree DFS: 针对树的深度度优先算法题**

**DFS在树上的遍历:** 此类题型考查基础遍历操作, 将不再新建文件, 直接在LeetCode中实现. 要求 1) 请仔细阅读完本介绍后十分钟内做完下面五道题 (很简单的). 2) 请在未来复习中再尝试使用非recursion方式解决此类遍历问题

- 144. 前序
- 94. 中序
- 145. 后序
- 589. N叉树前序
- 590. N叉树后序

**DFS在树上的路径问题:**

- 112. Path Sum (高频经典) (easy)
- 113. Path Sum II (med)
- 257. Binary tree paths (easy)
- 129. Sum root to leaf numbers (med)
- 437. Path Sum III (med)
- 124. Binary tree maximum path sum (hard)


**DFS构建/还原二叉树:**

- 105. Construct binary tree from preorder and inorder traversal (med)
- 106. Construct binary tree from inorder and postorder traversal (med)
- 889. Construct binary tree from preorder and postorder traversal (med)
- 108. Convert sorted array to binary search tree (easy)
- 109. Convert sorted list to binary search tree (med)




**DFS在树上的高频题:**

98 101 114 199 235 236 

**DFS 高频应用题:**
130 131 200 207 


## **参考链接 Reference:**

- https://www.jianshu.com/p/725de069938c (最好的BFS DFS详解)
- https://juejin.cn/post/6844904196685185038
- https://www.mscto.com/game/409337.html
