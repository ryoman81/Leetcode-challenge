# Pattern: Fast & Slow Pointers, 快慢指针类型

<img src="https://pic2.zhimg.com/80/v2-2a365e4768a0ed84683257d2364a6e71_720w.jpg?source=1940ef5c" />


## **解题思路:**

这种模式，有一个非常出门的名字，叫龟兔赛跑。这种算法的两个指针的在数组上（或是链表上，序列上）的移动速度不一样。这种方法在解决有环的链表和数组时特别有用。通过控制指针不同的移动速度（比如在环形链表上），这种算法证明了他们肯定会相遇的。快的一个指针肯定会追上慢的一个（可以想象成跑道上面跑得快的人套圈跑得慢的人）。

题型的特点是
- 需要处理环上的问题，比如环形链表和环形数组 
- 当你需要知道链表的长度或是某个特别位置的信息的时候 

什么时候使用快慢指针而不是双指针
- 在单链表上不能往回移动的时候: 例如 需要去判断一个链表是否是回文, 寻找链表中点位置等

## **解题步骤**
若题型符合快慢指针的题型
1. 设置快指针有多快

   快指针比慢指针快多少？这要看题目的条件，比方说如果题目要求链表最中间的结点值，我们可以设置快指针每次移动速度是慢指针的两倍，以后遍历事，慢指针一格一格移就行了，快指针两倍速的移即可。如果题目要求的是链表中倒数第 n 个结点，我们可以将快指针率先移动到正数第 n 个位置，以后慢指针从第 0 个开始，快指针从 n 开始同时遍历即可。

2. 开始同时遍历快慢指针

   遍历链表，快慢指针分别往后查找，直到 null，要求的结果就是慢指针指向的结点

3. 对于特定题型 141 和 142 还有之前做过的160 以及其他的扩展问题, 使用快慢指针在一个带有环的list上运行, 我们可以借助这个神图来了解他们走过的距离.

   <img src="https://images0.cnblogs.com/blog/354747/201311/05171805-64db9f059a1641e7afaf3dd8223c4fe7.jpg" />

   X: 起点位置
   
   Y: 环的结点位置
   
   Z: fast slow 相遇的位置

   当中的距离有某种神秘的关系!! 假定前提是fast = 2*slow 速度, 那么会有

   2(a+b) = a+b+c+b ===> **a = c**

   那么对几类延展问题便可以推断出:

   **环的节点:** 当fast从Z出发, slow从X出发, 以相同速度前行. 遇见之处就是结点
   
   **环的长度:** 从一开始fast, slow出发之后到在Z点遇见时,循环的次数即是环的长度
   
   **环的解套:** 根据上一点环的长度, 将指针走a+b+c-1步的那个结点处断裂即可解套

## **经典题目:**

- 19. Remove Nth node from end of list (med)
- 141. Linked list cycle (easy)
- 142. Linked list cycle II (med)
- 203. Remove linked list elements (easy)
- 876. Middle of the linked list (easy)

**非链表题型**
- 27. Remove element (easy)
- 283. Move zeros (easy)
- 202. Happy number (easy)

## **参考链接 Reference:**

- https://zhuanlan.zhihu.com/p/38521018
- https://www.cxyxiaowu.com/9726.html
- https://www.cnblogs.com/hiddenfox/p/3408931.html

## **模板 Template:**
### **Python**
```py
def fastSlowPointers (list):
   # usually we initial fast and slow pointers to the head of list
   fast = list
   slow = list
   # in some problem the fast pointer is advanced of slow pointer by n steps
   for i in len(n):
      fast = fast.next
   # then in a while-loop we usually check for either one of these purposes
   # 1. if fast catch up on the slow (for those cycle list)
   # 2. or if fast hit the tail
   while fast and fast.next:
      # advance fast and slow pointers in a speed ratio
      slow = slow.next
      fast = fast.next.next
      # do a conditional judgement
      if condition:
```