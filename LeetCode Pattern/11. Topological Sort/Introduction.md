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

0. 创建有向图的邻接表和入度表 (往往每道题当中关键点和难点在这个部分)
1. 遍历一个有向图, 这个有向图是没有回环的 (如果有, 不可进行拓扑排序, 返回False)
2. 用到和BFS一样的技术, Queue来存储待遍历的子节点, 使用iteration来不停的push和pop节点因而遍历整个图
3. 根据遍历返回对应结果, 存在环的图不可能完成所有的遍历, 因此需要根据题目要求返回False或其它东西

简单而言, 上述参考链接描述的算法叫做 Kahn's Algorithm 用到了 BFS+Queue 的技术. 对应的算法伪码请参考[reference 2](https://zhuanlan.zhihu.com/p/62582030) 和更为详细的 [reference 3](https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/)

上述过程当中涉及到几个关键概念, 我们以下面这个图做例子:
```
        [2] <------ [0]
        /  \
       /    \
      \/    \/
     [1]--->[3]
```

### **邻接表 adjacent list**
邻接表是表示图的一种方式, 这个在之前的课程当中学过. 还有一种表示方式叫做邻接矩阵, 在这个拓扑排序当中没有应用到. 邻接表常用hash table的形式表示. 上述图当中邻接表可以表示为:
```py
graph = {0: [2], 1: [3], 2: [1,3], 3:[]}
```

### **入度 in-degree**
**入度**这个词我也是在学习这个章节才第一次接触, 其实对应的还有个**出度 out-degree**. 这个在图当中的有向图可以很容易理解, 就是一个节点vertex被多少个箭头所指向的一个量化值. in-degree也用一个hash table来表达, 如示例当中
```py
indegree = {0:0, 1:1, 2:1, 3:2}
```

掌握了这两个关键概念之后, 目前做到的Topological Sort题型当中典型的207, 210, 269均可套用下面的模板来解决啦. 这类题型的难点不在于整个workflow是什么, 而是怎么根据题干的要求去构建邻接表和入度.

## **经典题目:**

- 207. Course schedule
- 210. Course schedule II
- 269. Alien Dictionary

下次做
- 444. Sequence reconstruction

## **参考链接 Reference:**

- https://www.jianshu.com/p/b59db381561a
- https://zhuanlan.zhihu.com/p/62582030 
- https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/ 

## **模板 Template**
```py
def topologicalSort (relationship):
  ## Step 1: initialize the indegree map and graph adjacent list
  # We only need to fill in empty thing
  graph = dict()
  indegree = dict()
  # The looping condition depends on problems
  for item in relationship:
    graph[item] = []
    indegree[item] = 0

  ## Step 2: construct indegree map and graph adjacent list 
  # The looping condition is also depending on problems where we can find origin ----> destination
  for origin, destination in relationship:
    graph[origin].append(destination)
    indegree[destination] += 1

  ## Step 3: use BFS+queue to traversal the graph
  queue = list()
  # Initialize queue with all node with indegree value 0
  for key in indegree:
    if indegree[key] == 0:
      queue.append(key)
  # Now we can do BFS search until queue empty
  # we may also step up result variables such as 'path' or 'count'
  path = [] 
  while queue:
    ## BFS: queue out: 
    # take out the current node and update result
    node = queue.pop(0)
    path.append(node)
    ## BFS: queue in: 
    # for the current node, find its all adjacent neighbors to whom the current node is pointing
    for neighbor in graph[node]:
      indegree[neighbor] -= 1
      # if find new zero-in-degree node, we push it to the queue
      if indegree[neighbor] == 0:
        queue.append(neighbor)

  ## Step 4: usually the final result should have the same length of all items
  if len(path) == len(indegree):
    return True
  else:
    return False
```

```js
function topologicalSort (relationship) {
  // Step 1: initialize the indegree map and graph adjacent list
  // We only need to fill in empty thing
  const graph = {};       // or const graph = new Map(), depends on which object you use
  const indegree = {};
  // The looping condition depends on problems
  for (let item of relationship) {
    graph[item] = [];
    indegree[item] = 0;
  }

  // Step 2: construct indegree map and graph adjacent list 
  // The looping condition is also depending on problems where we can find origin ----> destination
  for (let i = 0; i < relationship.length; i++) {
    const origin = relationship.origin;
    const destination = relationship.destination;
    graph[origin].append(destination);
    indegree[destination] += 1;
  }

  // Step 3: use BFS+queue to traversal the graph
  queue = []
  // Initialize queue with all node with indegree value 0
  for (let key of Object.keys(indegree)) {
    if (indegree[key] === 0) {
      queue.push(key);
    }
  }

  // Now we can do BFS search until queue empty
  // we may also step up result variables such as 'path' or 'count'
  const path = [];
  while (queue.length > 0) {
    // BFS: queue out: 
    // take out the current node and update result
    const node = queue.shift();
    path.push(node);
    // BFS: queue in: 
    // for the current node, find its all adjacent neighbors to whom the current node is pointing
    for (let neighbor of graph[node]) {
      indegree[neighbor]--;
      // if find new zero-in-degree node, we push it to the queue
      if (indegree[neighbor] === 0) {
        queue.push(neighbor);
      }
    }
  }

  // Step 4: usually the final result should have the same length of all items
  if (path.length === Object.keys(indegree).length) {
    return true;   // or something like traversal path
  } else {
    return false;  // or something
  }
}
```