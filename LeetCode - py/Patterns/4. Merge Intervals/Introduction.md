# Pattern: Merge Intervals, 区间合并类型

区间合并模式是一个用来处理有区间重叠的很高效的技术。在设计到区间的很多问题中，通常咱们需要要么判断是否有重叠，要么合并区间，如果他们重叠的话。这个模式是这么起作用的： 给两个区间，一个是a，另外一个是b。两个区间可能有如下图所示的六种情况

<img src="https://pic1.zhimg.com/80/v2-603053309be9d035b3c8ccee773e46e7_1440w.jpg?source=1940ef5c" />

这些问题从插入区间到优化区间合并都有。怎么识别啥时候用合并区间模式？
- 当你需要产生一堆相互之间没有交集的区间的时候 
- 当你听到重叠区间的时候

## **解题思路:**

Interval这个概念在算法题中时有出现, 就是一个区间(start, end)。可是这类题目做起来，却往往不那么简单。常见情况下, interval问题使用下面三个思路:
- **Sorting:** 在一般情况下，按照interval的start升序排序，在必要情况下，对于start相同的interval，按照interval的end的降序排序。
- **Greedy:** 有时候是两个interval之间的greedy，有时候是一群interval之间的greedy。
- *OTHER:* 用到了自平衡二叉树，比如c++里就是map，用红黑树实现的。当前两个思路不行时,考虑这个.

## **经典题目:**

- 56. Merge Intervals (med)
- 57. Insert Intervals (med)
- 252. Meeting Rooms (easy)
- 435. Non-overlapping Intervals (med)


**Other listed by the reference**

- 253. Meeting Rooms II (med)
- 452. Minimum Number of Arrows to Burst Balloons (med)
- 759. Employee Free Time (hard)
- 986. Interval List Intersections (med)

## **参考链接 Reference:**

- https://zhuanlan.zhihu.com/p/26657786
- https://www.paincker.com/leetcode-intervals 

## **模板 Template:**
### **Python**
```py

```