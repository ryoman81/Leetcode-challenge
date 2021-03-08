# Pattern: Backtracking: Subsets, Permutation, and Combination, 回溯法: 子集, 排列, 和组合问题
*起初这个topic名字是subsets, 原本以为是什么小类别. 嘿! 打开一看经典题型, 子集/排列/组合, 回溯法!! 这不就是大名鼎鼎的DFS recursion加回溯问题吗? 第一次面试惨遭失败的滑铁卢. 就是败在了permutation问题上. 惊喜! 终于做到你了. 赶紧进入正题*

回溯法 (backtracking) 是建立在 DFS 基础之上的应用算法, 因此它具有DFS的全部特性, recursion to solve the subproblem at the current moment, 以及recursion until nothing. 但回溯法最大的特性在于, backtracking会维持某一个状态然后进入recursion, 当从recursion返回后, 会恢复这个状态. 因此backtracking和普通的DFS区别在与, **有无状态重置**. 

状态重置的概念有点空虚. 但之前在DFS章节已经接触到了. 如果参考topic 8 DFS当中的路径遍历算法, 我们用了一个闭包内的变量path去存储当前路径中的节点们, 因此在递归函数当中, 我们做了两个相反的状态设置过程,

1. 进入递归函数时, path.append(node.val), 设置状态
2. 退出递归函数时, path.pop(node.val), 重置状态

这样的一组操作就是典型的backtracking pattern. 而第二步重置状态的操作, 我们称为**回溯**.

## **解题思路:**

网上看了好多教程不少需要用到比较晦涩的感念来讲解, 例如有关解空间, 决策树遍历等概念. 下方reference当中的第一二个讲解的十分明了. 我们可以通过 46, 77, 78三道题来理解整个流程. Backtracking的模板性十分强. 可以先看再做再回来总结. 

## **经典题目:**

所有题目都太经典了, 看到题目名字都能感觉到之前出现在Amazon面经当中. 全部是经典题目. 把下列列出的做干净之后, 务必需要把leetcode上backtracking tag刷干净.

- 46. Permutation (med)
- 47. Permutation II (med)
- 78. Subsets (med)
- 90. Subsets II (med)
- 77. Combination (med)
- 39. Combination Sum (med)
- 40. Combination Sum II (med)

**经典backtracking应用题**

- 22. Generate parentheses (med)
- 131. Panlindrome Partitioning (med)

- 51. N-Queens (hard) 超级经典题目
- 52. N-Queens II (hard)

- 79. Word Search (med)
- 44. Wildcard matching (hard)

- 37. Sudoku Solver (hard) 超级经典, 回溯法天花板 吃不下来就下次啦


## **参考链接 Reference:**

- https://www.cxyxiaowu.com/7103.html
- https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/ (all combinations and subsets problems)
- https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-ga-4/ (all permutations problems)
- https://blog.csdn.net/u011764940/article/details/105592965


## **模板 Template**
```py

```