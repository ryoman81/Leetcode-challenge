# Pattern: Dynamic Programming Problems, 动态规划问题
*有点像终极的武学宝典, 习得了two pointers, linked list, BFS/DFS, binary search, backtracking, 此刻心有所属的终极大山, 是时候该遇见了. **Hello DP!***

本章节为算法分类刷题的最后一章, (尽管它标注为0). 章节内容是涵盖广泛的dynamic programming. Introduction内讲解通用思路, 子文件夹按照最终选择的分类框架进行划分 (没办法, DP的题目简直太多了,而且只有应用题). 本章节选用的分类法来源于LeetCode圣诞大赛冠军的[帖子](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns), 在LeetCode上非常火. 

## **解题思路:**

解题思路的讲解根据的是这篇我觉得理解最为充分的[帖子](https://zhuanlan.zhihu.com/p/91582909).

动态规划的核心思想是, 例用历史数据 (cache) 实现记忆化 (memoization) *(这两个关键词在我们的interview课程当中出现过了)*. 说白点就是例用一个一维或二维数组 dp[ ] or dp[ ][ ]记录之前计算出来的一些结果(状态). 一般例用这些states去形成一个最优子结构 (optimal substructure). 白话讲就是一个子问题, 和recursion十分类似. 也因此top-down自上而下的DP解法就是使用recursion. 但本专题全部使用bottom-up自下而上的套路解决DP问题. 

三大主要步骤是,

### **1. State**
假设用一维数组 dp[] 保存从 i = 1, 2, ... k 时各个时期的状态。这个时候有一个非常重要的点，就是定义 dp[i] 是代表什么意思？通常 dp[n] 就是我们到达结果状态n时的解, 也就是题目所需的那个解. **因此, 你求什么, dp[n]它就是什么**

### **2. 确定状态转移 state transition**
~~读博士这么多年, 一直研究马尔可夫(Markov)过程~~, **好的, 小茗同学一语道破, 这不就是高中数学当中的归纳法嘛, 于是我默默地把前一句划掉了**, 状态转移即代表着从当前状态i-1转移到状态i的一个函数. 于是之前的state, 可以通过状态转移方程来到下一个, 例如
```
dp[i] = dp[i-1] + dp[i-2]
或
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

### **3. 确定初始值**
需要手动确定初始状态, 然后开始while循环, 从初始状态一路iterate到最终dp[n]状态. 常见的需要初始状态的点位包括: 

1. DP[0], DP[1]
2. DP[0][j], DP[i][0]
3. all DP[i], i < 0, 初始化成诸如MAX_INT, 因题而异

## **经典题目:**

**1. Distinct Paths 达到目标的路径/方式的总数**

- 70. Climbing stairs (easy)
- 62. Unique Paths (med)
- 63. Unique Paths II (med)
- 91. Decode Ways (med)
- 1155. Number of dice rolls with target sum (med)

**2. Minimum/Maximum cost to reach target 达到目标的最大/最小代价**

- 746. Min cost climbing stairs (easy)
- 64. Minimum path sum (med)
- 322. Coin change (med)
- 120. Triange (med)
- 983. Minumum cost for tickets (med)

## **参考链接 Reference:**

- https://www.zhihu.com/question/291280715 基本上全网大v(包括leetcode官号)的答案都在这个知乎帖子里面了, 各大v推广目的明显啊.
- https://zhuanlan.zhihu.com/p/91582909 详细的方法论, 个人觉得讲解最好的
- https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns LeetCode圣诞大奖得主的分类法, 我的分类就是按照这个的
- https://leetcode-cn.com/circle/article/2Xxlw3/ 另一个更为细致的分类标准

## **模板 Template**
```py

```