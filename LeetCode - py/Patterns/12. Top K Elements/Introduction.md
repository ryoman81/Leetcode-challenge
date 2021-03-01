# Pattern: Heaps & Top K Elements, 堆 和 前k个元素类型

开篇话, 原本在准备开启 Topic 9 Two Heaps 双堆问题. 后来发现问题本身没有什么特质, 更多是为了熟悉Heap这个数据结构. Topic 9当中本身有些有意思的题目, 后来发现全部都是本专题的内容. 因此判定 Topic 9 为酱油专题, 遂删去, 并与当前专题合并. 本专题首先讲解heap(最大堆/最小堆)的基本概念和用法, 进而讲解这一类用heap来解决的 前k个元素 一类问题的解题思路并归纳模板.


## **解题思路:**
### **Heap 堆**

Heap 堆的概念很简单, 就是要满足两个条件
1. 它是一颗完全二叉树 (complete binary tree). 所谓完全二叉树, 就是除了最底层, 上面都是满的 (一分二, 二分四, 四分八). 最底层如果摆不满, 也得从左向右摆放. 
2. 它的任意一个parent node都要大于(小于)它的children. 因此root一定是最大(最小)的.

堆的用处是让我们很容易知道一组数据当中的最大(最小)的一部分. 相比于线性结构, 堆的一些常见操作也能保持在树高的复杂度 O(H) 既 O(logn). 

堆的实现, 在很多语言中heap是通过array实现的. Java中使用PriorityQueue来实现heap的功能. Python中使用heapq模块实现最小堆. JS貌似没找到自带的heap数据结构. 但有关heap的题目当中, 大多数是自己手动实现heap的功能 (就像在sliding window当中我们自己用array构建了一个monoQueue单调队列一样)

鉴于Heap相关的题目当中, 你并不能直接引入heap这个数据结构(要不然考你什么?), 你需要自己实现heap的add, delete, search这几类常见的方法. 因此在做下列题之前, 请手动创建一个heap类! 

可以先看下简介, 然后自己实现一下(最小/最大都要), 如果行不通, 再看范例

Python: https://blog.csdn.net/qq_23869697/article/details/82735088
JS: https://blog.csdn.net/qq_43540219/article/details/108932367 

### **Top K Elements**

任何情况下, 让我们求解最大/最小/最频繁的K个元素问题都遵循这个专题的模式. 解题的过程是
1. 首先将输入array/string当中的前K个元素构建出一个最大/最小堆
2. 继续遍历输入当中剩下的元素, 将该元素与堆顶做比较来判断是否变更这个堆结构
3. 完成后返回这个堆中元素即为所求

案例示意, 如求[3,1,5,12,2,11] 当中最大的三个元素, 我们构建一个最小堆, 每次将新进的元素跟堆顶比较来判断是否需要变更这个堆. 
<img src="https://pic4.zhimg.com/80/v2-d42febfdf2d1ce2d2211e78ff8ea88db_720w.jpg?source=1940ef5c"/>


## **经典题目:**

- 215. kth largest element in an array
- 295. Find median from data stream
- 347. Top K frequent elements
- 378. kth smallest element in a sorted matrix

218 253 703 

## **参考链接 Reference:**

- https://www.mingtucareer.com/learn-heap/ 
- https://www.cnblogs.com/zhangwanying/p/9357141.html 
- https://blog.csdn.net/dingdingdodo/article/details/105935057 

## **模板 Template:**
### **Python**
```py
