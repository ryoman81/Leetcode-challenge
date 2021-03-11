'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false. 

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 
you should also have finished course 1. So it is impossible.
 
Constraints:
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def canFinish(self, numCourses, prerequisites):
    ## Step 1: initialize the indegree map and graph adjacent list
    # Here we use a hash table to build a adjacent list. (请参考之前网课图相关的基础知识)
    graph = dict()
    indegree = dict()
    for i in range(numCourses):
      graph[i] = []
      indegree[i] = 0

    ## Step 2: construct indegree map and graph adjacent list 
    for edge in prerequisites:
      graph[edge[1]].append(edge[0])
      indegree[edge[0]] += 1

    ## Step 3: use BFS+queue to traversal the graph
    queue = list()
    # Initialize queue with all node with indegree value 0 (把那些没有先决要求的课程推入队列)
    for i in range(numCourses):
      if indegree[i] == 0:
        queue.append(i)
    # Now we can do BFS search until queue empty
    # we use a counter to record how many courses finished
    count = 0
    while queue:
      ## BFS: queue out: take out the current node and count up
      node = queue.pop(0)
      count += 1
      ## BFS: queue in: for the current node, find its all connected nodes (child)
      for child in graph[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
          queue.append(child)

    #### lastly, we check how many courses we have taken
    if count == numCourses:
      return True
    else:
      return False
    

## Run code after defining input and solver
input1 = 3
input2 = [[1,0],[2,0],[2,1]]
solver = Solution().canFinish
print(solver(input1, input2))