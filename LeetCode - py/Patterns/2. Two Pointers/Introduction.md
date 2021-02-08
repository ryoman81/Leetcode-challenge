# Pattern: Two Pointers, 双指针类型

实际上, 双指针涵盖的范围非常广泛. 我们一直拖延没有进入这个topic也是因为很多其它题型都是双指针题型的特殊类别, 例如
1. Sliding window 滑动窗口类型题目
3. Fast & slow pointers 快慢指针类型题目
11. Binary Search 二叉搜索类型题目

所以! 自豪的讲, 我们双指针类型已经做了不少题目啦! 但不仅限于此, 根据更为广泛的双指针类型题目总结, 它被分为了
1. 左右指针：需要两个指针，一个指向开头，一个指向末尾，然后向中间遍历，直到满足条件或者两个指针相遇
2. 快慢指针：需要两个指针，开始都指向开头，根据条件不同，快指针走得快，慢指针走的慢，直到满足条件或者快指针走到结尾
3. 后序指针：常规指针操作是从前向后便利，对于合并和替换类型题，防止之前的数据被覆盖，双指针需从后向前便利

或者
1. 同向双指针
2. 反向双指针

不过如何的分类, 其实含义都是需要用到两个指针来搜索某个线性的空间. 相对应的题型又可以划分成为
1. sliding window
2. fast slow pointers (龟兔赛跑问题 部分此类问题在topic 5下可以用cyclic sort方法解决)
3. Sums problem (2sum 3sum...)
4. Sorting problem (一般用左右指针 包含了binary search问题下的)
5. partition
6. ... (还未总结)

根据材料经验, Sums problem 是非常高频的 (毕竟leetcode天字第一题就是2sum). 3Sums的变种特别多, 而且模板化程度也相对较高. 我倾向把这个topic未来的更多题型练习放在这类问题上. 


## **解题思路:**
还有啥思路, 种类这么多, 大类里面参考 sliding window, fast slow pointers, cyclic sort, and binary search 解题思路和模板! 请完成经典题型当中的, sums 和 同向双指针题目.

## **经典题目:**

**Sum 类型 (同向指针)**
- 167. Two Sum II in sorted array (easy)
- 15. 3Sum (med)
- 16. 3Sum Closest (med)

**同向双指针经典题目**
- 11. Container with Most Water (med)
- 42. Trapping Rain Water (hard)

**快慢指针类型 (已放入topic 3 快慢指针章节. 请回头去补充!)**
- 27. Remove element (easy)
- 283. Move zeros (easy)

## **参考链接 Reference:**

- https://blog.csdn.net/pushup8/article/details/85071735
- https://turingplanet.org/2020/05/20/array-two-pointers%E5%A5%97%E8%B7%AF%E3%80%90leetcode%E5%88%B7%E9%A2%98%E5%A5%97%E8%B7%AF%E6%95%99%E7%A8%8B2%E3%80%91/
- https://jolie1191.github.io/2018/05/09/Two%20Pointer%20%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93/
- https://juejin.cn/post/6844903881588080648

## **模板 Template:**
仅仅是一些思路, two pointers 涵盖的题型太过广泛, 其他章节已经涉及到了不少. 这一章节题目全部都是两边夹击型的双指针. 对 Sums 和 经典题型, two pointers 往往是在一个数组 (很可能是排序好的数组) 两头进行. 移动pointer的原则往往根据题目来判断. while (left < right) 则是最外层的大循环.