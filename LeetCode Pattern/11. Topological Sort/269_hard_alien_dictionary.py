'''
There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,
[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,
[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    The overall procedure follows the same template of course schedule that
      1. we first initialize and construct indegree map and graph adjacent list
      2. we use queue+BFS to traversal the graph
      3. before returning we check if finally result is valid
    The pain point in this problem is constructing the adjacent list.
      - Differ from course schedules problems, the constructing process is very TROUBLESOME
      - The details are presented via comments. Please understand it thoroughly
  Complexity:
    Time: O()
    Space: O()
  '''
  def alienOrder(self, words):
    # initialize graph and indegree map
    graph = dict()
    indegree = dict()
    for word in words:
      for char in word:
        if char not in graph:
          graph[char] = []
          indegree[char] = 0

    # create graph and indegree map
    # This part is this question-oriented and VERY hard to complete instantly for this question
    for i in range(len(words)-1):
      # for outlayer loop, we take every neighboring words to compare
      word1 = words[i]
      word2 = words[i+1]
      for j in range(len(word1)):
        # for this innerlayer loop, we characters from two words at the same index
        # since we iterate from the first word, we should consider the different lengths of two words
        char1 = word1[j]
        char2 = ''
        # if the length of word2 is longer than word1, it doesn't matter
        # 因为word2当中相比word1多出的那一段不会影响到建立这个图的邻接表的关系
        # 但word1比word2长的话, 这就有可能出现问题, 这个判断将在下面展现
        if j < len(word2):
          char2 = word2[j]
        # once we took out char1 and char2 from word1 and word2 at the index j, we should do comparison
        # --> if they are the same, we do nothing but move to the next index of j
        # --> if they are different, we may create their relationship in the adjacent list
        if char1 != char2:
          # !! Here is the important part. Think if at index j, word1 has char1, but word2 has nothing
          # for example: word1: 'abcde'; word2: 'abc'; j=3. Then word1 is invalidly shown before word2
          # 按照字典序列排序规则, abcde是abc的子集, 因此在新华字典里面应该先出现abc, 然后后面的条目再出现abcde
          if not char2:
            # hence we return function
            return ''

          # if everything is valid, then we can construct the relationship such that char1 ---> char2
          # However, before that we should have a final check if char2 has already existed in char1's group
          # 当邻接表当中条目 char1: [a, b, c...] 当中已经存在char2的话, 这个关系已经添加进去了, 因此就不再需要重复添加并自增indegree的值
          if char2 not in graph[char1]:
            graph[char1].append(char2)    # add char2 to char1's adjacent list
            indegree[char2] += 1          # increment char2's indegree
          # finally we should stop the comparison of following char1 and char2 (跳出内循环)
          # because the current char1 and char2 are different, the following char1 and char2 cannot establish a relationship anymore
          break

    # initialize queue with all items of zero-indegree
    queue = []
    for key in indegree:
      if indegree[key] == 0:
        queue.append(key)
    
    # starting BFS 
    path = []
    while queue:
      char = queue.pop(0)
      path.append(char)
      for item in graph[char]:
        indegree[item] -= 1
        if indegree[item] == 0:
          queue.append(item)
    
    # return path if the length matches
    if len(path) == len(indegree):
      return ''.join(path)
    else:
      return ''
    

## Run code after defining input and solver
input = [
  'abc',
  'abcxdfg'
]
solver = Solution().alienOrder
print(solver(input))