# A high-level summary of round two preparation

A figure from Zhihu as the guidance for the classification when entering level of 300-500 questions. Please follow LeetCode tag and sort in frequency. If solved before, review and check the highlights. Otherwise, resolve it. 

<img src="https://pic1.zhimg.com/80/v2-70b07cab3afb34421e0ea5b5bcab8089_720w.jpg?source=1940ef5c" />

In details, the daily exercises include
1. Review the topic and template of this classification.
2. Move on LeetCode list in current tag. Review the solved questions, and try to finish unsolved questions in timely manner. 
3. 2 in the morning, 4 in the afternoon. After break time, 2 more. Evening 2 with Ming in the manner of mocking interview. 

Follow several principles,
1. Figure the frame out in 10 minutes or refer to the solution.
2. Speak loud when thinking, framing up the problem, asking potential questions, and asking for the hints. (自己跟自己说虽然比较傻...)
3. Watch out the time elapsed everytime. Pretent to have a real inverview during the night time. 
4. If stalled, go and take a look at OOP and BQ instead of schrolling iPhone......

# Classification
## Binary Tree
树上的问题, 检查树, 翻转树, 遍历树, 重建树等问题. Refer to topic 1 and 2 in Pattern folder.

### Notes
1. BST 是考察的重点. BST深入理解in-order traversal的应用.
2. BST 当中predecessor and successor的概念. node的succesor在node.right.left.left...., node的predecessor在node.left.right.right....
3. Lowest common ancestor (LCA) 问题, 可以从p, q起始, 也可以从root出发.
4. !!树上问题通常都要切分成子问题, 然后理解子问题form up以及transit的过程. 绝大多数树上问题都要找到能够切分的子问题.

### Logs
- 2021.7.26: tag binary tree, sorted in frequency, **14** in total.
- 2021.7.27: tag binary tree, sorted in frequency, **11** in total.

## Gpaph and Topological Sort
图上连接, 以及拓扑排序的应用问题. Refer to topic 1, 2, and 11 in Pattern folder.

### Notes
1. 涉及到图上的问题, 都需要构建邻接表 adjacent list 或邻接矩阵
2. 只有BFS的解法需要用到in-degree入度表, DFS解法不需要入度表
3. 遍历邻接表的基本算法输入DFS BFS问题，常见需要使用visited存储已访问节点

### Log
- 2021.7.28: tag graph, sorted in frequency, **6** in total.
- 2021.7.29: tag graph, sorted in frequency, **6** in topic, **3** of casual problems.
- 2021.7.30: tag graph, sorted in frequency, **4** in topic, **3** of casual problems.

### Ref
https://www.paincker.com/graph-theory

## DFS and Backtracking
深度优先及回溯相关问题, 与前两问题重叠相通。

### Log
2021.7.28


# Reference
1. https://www.zhihu.com/question/321738058/answer/1252502958
2. https://github.com/resumejob/Leetcode-retag
3. https://zhuanlan.zhihu.com/p/349940945