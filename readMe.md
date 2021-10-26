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

## Gpaph and Topological Sort
图上连接, 以及拓扑排序的应用问题. Refer to topic 1, 2, and 11 in Pattern folder.

### Notes
1. 涉及到图上的问题, 都需要构建邻接表 adjacent list 或邻接矩阵
2. 遍历邻接表的基本算法输入DFS BFS问题，常见需要使用visited存储已访问节点
3. Unweighted, undirected 问题一般使用DFS比较好判断链接状态, 例如有多少个独立节点, 是否有cycle, 一定需要visited记录访问过的节点. 如果非backtracking形式, 及返回recursion时未消除visited, 则需要有单独判断是否为parent node的语句.
4. Tarjan's algorithm: unweighted, undirected, **find the cycle in graph**. 专用在1192上. 需要为每个节点设置一个rank. 使用dfs, 当邻接点是已访问过的, 且rank高于自己的点时, 检测到cycle. ranks同样扮演visited角色, 记录已访问过的节点.
5. Kahn's algorithm: unweighted, directed, can be cyclic, **topological sort to find the linear dependence of all nodes**. 用在201 207, 310上, 需要使用in-degree和adjacent list, 邻接表反写graph[des] = [src1, src2...] 从入度为0的node起始, 每次减少其相邻的nodes的入度.
6. Bipartition algorithm: 染色问题, 用在unweighted, undirected图上. LC 886, 785. visited记录染色情况, 0未着色, 1 -1代表相反着色. 递归函数记录当前点应着颜色. 最外层遍历所有未着色节点并调用递归. BFS 使用方法类似.
7. Kruskal's algorithm: undirected, weighted graph, **find the minimum spanning tree (MST)**. 从图中生成带权重的最小生成树算法. 题1135. 按权重排序, 然后从最小权重的边开始链接, 并检查是否成环. 直到node-1个环安排上. 需要借助一个parent表, 在每次添加连接时, 更新parent表指向当前的根节点. 如果两个城市的根节点一致的情况下, 连接两个城市势必造成环.

### Ref
https://www.paincker.com/graph-theory

## Backtracking
回溯问题现在发现尽管都是dfs模板上手, 但对于边界条件, 变量传递等, 每道题的实现都没法达成模板统一化, 而且问题框架的设定, 说明白一道问题的能力都很有考研. 

## Trie 字典树
新的数据结构, 在第一轮时没有遇到过. 使用场景用在 **字符串**, **搜索树**, **字符前缀**, 这些关键概念上. 关键题目是 140 Word Break II, 212 Word Search II, 用于匹配字符串. 

### Notes
1. Trie is implemented by hash map and represented in tree structure. A trie is a dictionary of a group of words. The searching and inserting time complexity are O(k) where k is the length of the word (or the height of the tree).
2. Strings in the same path have same prefix. Trie node may have a **KEY_WORD** flag. When iterate to a node, who has a key_word, it denotes a complete word from root to this location. Usually store this word at this key.
3. 212题揭示了, 我们创建的trie不一定需要有search方法, 可能需要根据遍历的路径来iterate trie pointer. (trie search is mixed with recursive step, a parent node is passed)
4. Trie 常见的 O(k) 操作是, insert, search, 还有需要搭配用到DFS的search_prefix, 即找到从prefix起始的所有符合条件的match.


# Reference
1. https://www.zhihu.com/question/321738058/answer/1252502958
2. https://github.com/resumejob/Leetcode-retag
3. https://zhuanlan.zhihu.com/p/349940945