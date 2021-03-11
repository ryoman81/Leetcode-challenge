'''
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] 
this means you must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, 
return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 
you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have 
finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
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
  def findOrder(self, numCourses, prerequisites):
    # Initialize graph representation and indegree table
    graph = dict()
    indegree = dict()
    for i in range(numCourses):
      graph[i] = []
      indegree[i] = 0

    # create graph adjacent list and indegree map
    for edge in prerequisites:
      graph[edge[1]].append(edge[0])
      indegree[edge[0]] += 1

    # Do BFS using a queue
    queue = list()
    path = []

    # Initialize queue with all node with indegree value 0\
    for i in range(numCourses):
      if indegree[i] == 0:
        queue.append(i)

    while queue:
      ## BFS: queue out: take out the current node and push to the result path
      node = queue.pop(0)
      path.append(node)

      ## BFS: queue in: for the current node, find its all connected nodes (child)
      for child in graph[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
          queue.append(child)

    # Check how many courses we have taken
    if len(path) == numCourses:
      return path
    else:
      return []
    

## Run code after defining input and solver
input1 = 3
input2 = [[1,0],[2,0],[2,1]]
solver = Solution().findOrder
print(solver(input1, input2))