# Pattern: Breadth First Search, 广度优先搜索

## **类别总结:**
广度优先算法 BFS 是一类搜索算法大的框架, 题型涉及到对树直接的操作, 广度搜索图Graph, 走迷宫等等. 涵盖的思路是以联通节点单个层进行搜索遍历, 完成后再进入下一层. 第一次刷题总结, 我们针对 Tree Search先行实践BFS 算法的特性和代码套路. 后续深入学校再进行其他高频题型的扩充.

## 1. 树上的BFS
这种模式基于广度优先搜索（Breadth First Search (BFS)），适用于需要遍历一颗树。借助于**队列**数据结构，从而能保证树的节点按照他们的层数打印出来。打印完当前层所有元素，才能执行到下一层。所有这种需要遍历树且需要一层一层遍历的问题，都能用这种模式高效解决。

这种树上的BFS模式是通过把根节点加到队列中，然后不断遍历直到队列为空。每一次循环中，我们都会把队头结点拿出来（remove），然后对其进行必要的操作。在删除每个节点的同时，其孩子节点，都会被加到队列中。 

识别树上的BFS模式： 如果你被问到去遍历树，需要按层操作的方式（也称作层序遍历）

<img src="https://upload-images.jianshu.io/upload_images/10107787-b9da64a7c631e0e6.gif?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp" />

## **经典题目:**

**Tree BFS: 针对树的广度优先算法题**

- 102. Binary tree level order traversal (med)
- 103. Binary tree zigzag level order traversal (med)
- 107. Binary tree level order traversal (bottom-up) (easy)
- 429. N-ary tree level order traversal (med)

- 111. Minimum depth of binary tree (easy)
- 513. Find bottom left tree value (med)

**The Maze: 迷宫题**

- 490 505 499

**BFS 应用及其它树的高频题**

- 127 130 199 200 207 279 286 310 863

## **参考链接 Reference:**

- https://www.jianshu.com/p/725de069938c (最好的BFS DFS详解)
- https://www.cnblogs.com/zhangwanying/p/9706908.html (leetcode BFS题目汇总)
- https://shawnlyu.com/algorithms/intro-to-graph-algorithms-bfs-dfs/
