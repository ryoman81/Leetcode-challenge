# Pattern: Topological Sort, 拓扑排序
终于来到了最后一个章节 (除DP外) 经过了两个月时间, 走过了60-75道新题跨越了11个类别 (按照原先分类是13个). 废话不多说, 本章节拓扑排序, 是个大酱油! 基本只为了一道经典题型而设立, Course Schedule. 

## **解题思路:**

**拓扑排序就是BFS**. 定义为:
```
给定一个有向图(没有环的), 图当中的拓扑排序定义为:
- 对所有的 nodeA -> nodeB, A必须排在B的前面
- 排序当中的第一个元素必须为 '没有其它元素指向的'
```

请看下面这个案例, 给定一个有向图:
<img src='https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tZWRpYS1jZG4uaml1emhhbmcuY29tL21hcmtkb3duL2ltYWdlcy84LzYvOTFjZjA3ZDItYjdlYS0xMWU5LWJiNzctMDI0MmFjMTEwMDAyLmpwZw?x-oss-process=image/format,png' />

它的拓扑排序就为: 
```
[0,1,2,3,4,5] or
[0,2,3,1,5,4] or
...
```

是不是很显然, 对一个有向图, 它的拓扑排序就是BFS按照层搜索遍历的结果. 更为宽松的条件就是, 它不在乎单个层当中的顺序是 [1,2,3] 还是 [3,1,2]. 它只需要按层序遍历就行. 因此拓扑排序的要点是,

1. 遍历一个有向图, 这个有向图是没有回环的 (如果有, 不可进行拓扑排序, 返回False)
2. 用到和BFS一样的技术, Queue来存储待遍历的子节点, 使用iteration来不停的push和pop节点因而遍历整个图
3. 结果当中, 父节点永远在子节点的前面. 并不在意同一层当中子节点的摆放顺序

对应的算法伪码请参考[reference 2](https://zhuanlan.zhihu.com/p/62582030) 和更为详细的 [reference 3](https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/)

简单而言, 上述参考链接描述的算法叫做 Kahn's Algorithm

## **经典题目:**

- 207. Course schedule
- 210. Course schedule II
- 269. Alien Dictionary
- 444. Sequence reconstruction

## **参考链接 Reference:**

- https://www.jianshu.com/p/b59db381561a
- https://zhuanlan.zhihu.com/p/62582030 
- https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/ 

## **模板 Template**
```py

```