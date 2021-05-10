# Stock Problems 股票买卖问题及利益最大化问题

该问题分类主要围绕一系列热门问题, Best time to buy and sell stock. 另198题也归入该类型下, 尽管它和topic 2更为相似. 但是所有的买卖股票问题有非常强的模板性. 需要理解背后泛化的(generalization) DP内涵, 以及针对不同问题变种的优化形式. 此类题经典且热门, 因此列出该专题的详细解释.

## **Problem Description**

股票买卖问题一共六道,

- 121. Best time to buy and sell stock (easy)
- 122. Best time to buy and sell stock (med)
- 123. Best time to buy and sell stock III (hard)
- 188. Best time to buy and sell stock IV (hard)
- 309. Best time to buy and sell stock with cooldown (med)
- 714. Best time to buy and sell stock with transaction fee (med)

其中188为所有题目的终极泛化题. 模板也是通过它设计出来的. 其余所有题都有space complexity optimization形式, 因此需要了解透彻之后, 对应简化.

题目通常的如此表述:

1. 给定一个prices数组, prices[i] 为 stock price in the ith day
2. 题目寻求的是找到一组买卖的策略达到利润最大化
3. 此类题型的变量包括, **交易日期, 总交易次数, 以及 买/卖 两种行为.** 

## **Constructing DP 定义DP数组**

我们根据问题描述, 以及题目当中涉及到的变量, 设计出一个generalized DP
```py
DP[i][k][x]

# i - at the ith day, [0, n-1]
# k - the number of trading has been conducted till ith day, [0, K]
# x - 0 or 1, if holding a stock or not, 0 || 1
```
据此, DP[i][k][x] 表示的是, 在第i天, 总共交易过最多k次, 此时有或没有股票在手中时, 获得的**最大的利润**.

## **Returning value 最终返回值**

题目全部所求的是, 经历过所有天数, 完成**最多**K次交易情况下, 能获得的最大收益, 即
```py
DP[n-1][K][0]
```

## **State transition 状态转移**
状态转移是本问题最复杂的地方, 根据该模板可以写出以下转移方程
```py
# 当前第i天, 已经交易过最多k次, 且现在手头没有股票
# 该情况下的DP分为两种情况, 
  # a)前一天手头也没有股票, 但今天未有交易; 
  # b)前一天手头有股票, 但我把它卖了 
DP[i][k][0] = max(DP[i-1][k][0], DP[i-1][k][1] + prices[i])

# 当前第i天, 已经交易过最多k次, 且现在手头有股票
# 该情况下的DP同样分为两种情况, 
  # a)前一天手头也有股票, 但今天未有交易; 
  # b)前一天手头没有股票, 但今天产生了交易 
DP[i][k][1] = max(DP[i-1][k][1], DP[i-1][k-1][0] - prices[i])

# 牢记!! DP是当前的利润!!
```

## **Initialization 初始化**
因为DP数组涉及到三个变量的维度, 初始化时考虑比较复杂. 一个策略是将DP的第三个维度分解成两个二维数组. 即, 
```py
DP0[i][k]   # 第i天经历了最多k次交易后手头没有股票状态下的最大收益
DP1[i][k]   # 第i天经历了最多k次交易后手头有股票状态下的最大收益
```
最终所求是 DP0[n-1][K], 即经历了n-1天后, 最多K次交易, 在手头没有股票的状态下, 最大的收益.

根据这个表述, 需要初始化 i=0, k=0的两类场景. 
```py
DP[0][0][0] = 0
```

## References
- !最好贴 https://medium.com/@USTCLink/%E7%A7%92%E6%9D%80%E9%9D%A2%E8%AF%95%E4%B8%AD%E7%9A%84%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98-%E7%9C%8B%E8%BF%99%E4%B8%80%E7%AF%87%E5%B0%B1%E5%A4%9F%E4%BA%86-fa730ae4681d
- https://zhuanlan.zhihu.com/p/105760677
- https://zhuanlan.zhihu.com/p/92908822