# Pattern: LinkedList, 链表

这个章节原本内容只是和链表的反转相关的topics. 但是为了针对链表这个tag进行更深入的理解和学习, 我将此扩展到Leetcode上LinkList相关的更多题型. 借此对链表该数据结构和相关的题型能有更深入的理解和归纳. 

LinkedList 题型无非涵盖了基础操作: **增, 删, 改, 查**, 以及常见的操作包括: **反转, 合并**. 理解链表数据解构是关键. 详情请回顾之前网课课程当中的介绍. 在本章节内, 我们先自己写一个linkedlist的基本数据结构作为公共类. 其余实现需求(增删改查反转合并) 皆根据不同题型进行学习和编写. 最终要点会总结在该文档模板之内. 

## **经典题目:**

- 21. Merge two sorted lists (easy)
- 23. Merge k sorted lists (hard)
- 148. Sort list (med) [move to topic 3]
- 160. Intersection of two linked list (easy)
- 206. Reverse linked list (easy)
- 234. Palindrome linked list (easy)
- 237. Delete node in a linked list (easy)

**其它题目**
2 19 25 61 82 83 86 92 141 142 

## 个人经验总结

三天快速把所有基础的linked list 题目都做了一遍, 虽然很多是easy题目, 但是对独特的数据结构, 还是很多操作不方便. 最大的特点就是无法按照index 索引某一项. 任何情况下都只能通过next去推进
有两个特殊点可以总结:
- 题目21, 合并两个sorted lists被当作通用的方法运用在了sorting 和 merge k这两道常用题当中. 也因此这三道题成为了非常高频的题目
- 对list的翻转, 删除节点的操作都是通过修改.next指针来完成, 因此多多回顾这几道题, 以及之前学习中的linkedlist data structure

本topic就不设计通用模板了

## **参考链接 Reference:**

- https://leetcode.com/problemset/all/?topicSlugs=linked-list&listId=wpwgkgt