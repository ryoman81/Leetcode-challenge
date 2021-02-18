# Pattern: Depth First Search, 深度优先搜索

起初准备这个类别时, 当作和BFS类似的练习方式, 先通过对树上的DFS一众操作的学习, 加深了解, 再扩展到其它高频的应用. 但经过一番探索之后, 感觉DFS下的问题框架很庞大, DFS更加抽象成一种操作思维, 从而延展到几乎 recursion, backtracking, 还有很多DP问题的基础思维都要用到DFS去处理. 因此, 这个章节应该是所有topic当中最为庞大和复杂的类型 (毕竟Leetcode上DFS tag就有四页, 超过两百道题目了~)

## **类别总结:**
同上一个BFS类似, 在第一轮的总结归纳中, 我们希望对基本的在树上的DFS操作进行第一轮总结学习. 而后, 需要细致总结backtracking回溯法问题, Recursion的基本规范, 以及广泛高频题 (迷宫, 二维矩阵, 岛等应用题)的总结学习.

## 1. 树上的DFS
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

## **经典题目:**

### **Tree DFS: 针对树的深度度优先算法题**

**DFS在树上的遍历:** 此类题型考查基础遍历操作, 将不再新建文件, 直接在LeetCode中实现. 要求 1) 请仔细阅读完本介绍后十分钟内做完下面五道题. 2) 请在未来复习中再尝试使用非recursion方式解决此类遍历问题

- 144. 前序
- 94. 中序
- 145. 后序
- 589. N叉树前序
- 590. N叉树后序

**DFS在树上的路径问题:**

**DFS在树上的祖先问题:**


## **参考链接 Reference:**

- https://www.jianshu.com/p/725de069938c (最好的BFS DFS详解)
- https://juejin.cn/post/6844904196685185038
- https://www.mscto.com/game/409337.html


## **模板 Template:**
### **Python**
```py
```