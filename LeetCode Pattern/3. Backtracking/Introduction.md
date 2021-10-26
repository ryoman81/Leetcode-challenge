# Pattern: Backtracking: Subsets, Permutation, and Combination, 回溯法: 子集, 排列, 和组合问题
*起初这个topic名字是subsets, 原本以为是什么小类别. 嘿! 打开一看经典题型, 子集/排列/组合, 回溯法!! 这不就是大名鼎鼎的DFS recursion加回溯问题吗? 第一次面试惨遭失败的滑铁卢. 就是败在了permutation问题上. 惊喜! 终于做到你了. 赶紧进入正题*

回溯法 (backtracking) 是建立在 DFS 基础之上的应用算法, 因此它具有DFS的全部特性, recursion to solve the subproblem at the current moment, 以及recursion until nothing. 但回溯法最大的特性在于

### **1. 状态重置**
backtracking会维持某一个状态然后进入recursion, 当从recursion返回后, 会恢复这个状态. 因此backtracking和普通的DFS区别在与, **有无状态重置**.

状态重置的概念有点空虚. 但之前在DFS章节已经接触到了. 如果参考topic 8 DFS当中的路径遍历算法, 我们用了一个闭包内的变量path去存储当前路径中的节点们, 因此在递归函数当中, 我们做了两个相反的状态设置过程,

1. 进入递归函数时, path.append(node.val), 设置状态
2. 退出递归函数时, path.pop(node.val), 重置状态

这样的一组操作就是典型的backtracking pattern. 而第二步重置状态的操作, 我们称为**回溯**.

### **2. 剪枝**
大多数backtracking题目需要prune, **剪枝**. Pruning本质上就是recursion的base case, 通常放在for-loop内, 执行下一次recursion() 之前做条件判断, 如果该条路径的解已经不存在了, 即跳过该循环. Pruning也可放在递归函数起始, 和base case充当一样的条件判断, 不成立则可立即返回当前递归.

Pruning是很多backtracking题目(还有面试)当中考察的重点, 如果没有对搜索路径的修剪, 那就是纯粹的穷举, 有些leetcode题目(79)会专门设置非常测试极端的例子来考察当前算法有无pruning. 通常需要考虑的例子包括:

- 搜索空间给出的方向是否超出界限 (之前DFS已经遇到的迷宫问题)
- 搜索空间给出的所有方向是否存在无效的(例如已经访问过并不可再访问的节点)
- 在当前条件下是否可以通过某种判断推测出继续递归肯定也找不到答案了

## **解题思路:**

网上看了好多教程不少需要用到比较晦涩的感念来讲解, 例如有关解空间, 决策树遍历等概念. 下方reference当中的第一二个讲解的十分明了. 我们可以通过 46, 77, 78三道题来理解整个流程. Backtracking的模板性十分强. 基本都遵循同样的套路, 下面是一个pseudocode. 详细的代码模板参考最后.
```py
result = []       # 总的结果集
path = []         # 路径的记录
state variables   # 一些状态变量来判断是否剪枝
# 这些状态变量同样也可以通过参数传给回溯函数, 实际题目中有些混用.

def backtracking ():
  if 结束条件:
    更新/记录结果

  for 选择 in 搜索列表:
    if 选择 not 题目条件:       # ----> 剪枝 [这个判断过程也可放在for外面]
      continue
    设置状态                    # ----> 设置状态
    backtracking()             # ----> 进入递归
    还原状态                    # ----> 还原状态

backtracking()
return result
```

## **经典题目:**

所有题目都太经典了, 看到题目名字都能感觉到之前出现在Amazon面经当中. 全部是经典题目. 把下列列出的做干净之后, 务必需要把leetcode上backtracking tag刷干净.

(根据题解, 貌似这几个题的时间上限都是 n * 2^n. 有点数学意味, 说是一个宽松上限, 没深入了解)

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
- 79. Word Search (med)
- 51. N-Queens (hard) 超级经典题目

下次再做题目

37 Sudoku Solver (hard) 超级经典, 回溯法天花板, 巨难

44 Wildcard matching (hard) 亚麻原题, 不止backtracking一种解法

10, 60, 89, 93, 126, 140, 212, 401, Other combination sum 题目...

## **参考链接 Reference:**

- https://www.cxyxiaowu.com/7103.html
- https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/ (all combinations and subsets problems)
- https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-ga-4/ (all permutations problems)
- https://blog.csdn.net/u011764940/article/details/105592965


## **模板 Template**
```py
def problem (nums):
  # 通常回溯法的例题都使用闭包形式, 而不是直接原题函数进行递归.
  # 因为很多情况下backtracking比纯DFS题目要来的复杂, 考虑的东西更多.
  # Set up some closure variables outside the backtracking function
  result = []
  path = []
  # other helping variables for recording and pruning, such as count, ifUsed...
  state = xxx

  # Define a backtracking recursive function
  def backtracking (someStateToCarry):
    # the base case that meet the requirement of this problem
    # 回溯法的特点是, 通过剪枝, 维护的path始终是一个valid路径
    # 因此判断path是否满足条件, 不应该出现在base case当中, 而应该在剪枝过程中
    if len(path) == len(nums):
      result.append(path[:])
      return
    
    # search for all possible solutions
    # [KEY STEP] we need to set up a solution list for each problem
    # choices是总共解的空间, 代表每次在递归函数当中搜寻下一步路径的范围: 例如走迷宫就是四个方向
    for i in range(choices):
      # [KEY STEP] Pruning
      # we should avoid recursing if some scenarios meet
      # 剪枝通常发生在这里, 这个解的空间可能在某些时候已经没有搜索下去的必要了
      # 例如走迷宫的时候遇到了墙, 或者下一次搜索的点已经遍历过了
      if state condition: continue

      # [KEY STEP] Set current state
      # 包括存储路径, 记录某个点, 计数器加1, 或标记当前点为已访问
      path.append(choices[i])
      # do recursion from current node
      # we may update some state to carry out such as, starting index...
      backtracking(updateStateToCarry)
      # [KEY STEP] Restore current state: 状态重置: 好比取消当前点已访问的tag...
      path.pop()

  # Start backtracking recursion.
  # If there is some state to carry out for the next recursion we can set it here.
  # 实际上backtracking函数的的参数全部可以放在闭包里面, 看不同题目的使用习惯, 这两者是等价的
  backtracking(initialStateToCarry)
  # Return problem function
  return result
```