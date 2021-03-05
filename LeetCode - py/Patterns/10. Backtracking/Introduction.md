# Pattern: Backtracking: Subsets, Permutation, and Combination, 回溯法: 子集, 排列, 和组合问题
*起初这个topic名字是subsets, 原本以为是什么小类别. 嘿! 打开一看经典题型, 子集/排列/组合, 回溯法!! 这不就是大名鼎鼎的DFS recursion加回溯问题吗? 第一次面试惨遭失败的滑铁卢. 就是败在了permutation问题上. 惊喜! 终于做到你了. 赶紧进入正题*

回溯法 (backtracking) 是建立在 DFS 基础之上的应用算法, 因此它具有DFS的全部特性, recursion to solve the subproblem at the current moment, 以及recursion until nothing. 但回溯法最大的特性在于, backtracking会维持某一个状态然后进入recursion, 当从recursion返回后, 会恢复这个状态. 因此backtracking和普通的DFS区别在与, 有无状态重置. 

上面对状态选择, 和状态重置的概念有点空虚. 但之前在DFS章节已经接触到了. 如果参考topic 8 DFS当中, 路径遍历的算法, 

## **解题思路:**


## **经典题目:**

所有题目都太经典了, 看到题目名字都能感觉到之前出现在Amazon面经当中. 全部是经典题目. 把下列列出的做干净之后, 务必需要把leetcode上backtracking tag刷干净.

- 46. Permutation (med)
- 77. Combination (med)
- 78. Subsets (med)
- 47. Permutation II (med)
- 39. Combination Sum (med)
- 90. Subsets II (med)

**经典backtracking应用题**
- 22. Generate parentheses (med)
- 37. Sudoku Solver (hard)
- 44. Wildcard matching (hard)
- 51. N-Queens (hard) 超级经典题目
- 52. N-Queens II (hard)


## **参考链接 Reference:**

- https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/
- https://blog.csdn.net/u011764940/article/details/105592965

## **模板 Template**
