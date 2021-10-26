# Pattern: Sliding window, 滑动窗口类型

<img src="https://pic4.zhimg.com/80/v2-ec5aa95052f81e22fed272c87c423653_720w.jpg?source=1940ef5c" />


## **解题思路:**

滑动窗口这类问题一般需要用到双指针来进行求解，另外一类比较特殊则是需要用到特定的数据结构，像是 sorted_map。后者有特定的题型，后面会列出来，但是，对于前者，题形变化非常的大，一般都是基于字符串和数组的，所以我们重点总结这种基于双指针的滑动窗口问题。

题目问法大致有这几种：

- 给两个字符串，一长一短，问其中短的是否在长的中满足一定的条件存在，例如：
   - 求长的的最短子串，该子串必须涵盖短的的所有字符
   - 短的的 anagram 在长的中出现的所有位置
- 给一个字符串或者数组，问这个字符串的子串或者子数组是否满足一定的条件，例如：
   - 含有少于 k 个不同字符的最长子串
   - 所有字符都只出现一次的最长子串

除此之外，还有一些其他的问法，但是不变的是，这类题目脱离不开主串（主数组）和子串（子数组）的关系，要求的**时间复杂度往往是O(n)，空间复杂度往往是常数级的**。之所以是滑动窗口，是因为，遍历的时候，两个指针一前一后夹着的子串（子数组）类似一个窗口，这个窗口大小和范围会随着前后指针的移动发生变化。

根据前面的描述，滑动窗口就是这类题目的重点，换句话说，窗口的移动就是重点。我们要控制前后指针的移动来控制窗口，这样的移动是有条件的，也就是要想清楚在什么情况下移动，在什么情况下保持不变，我在这里讲讲我的想法，**思路是保证右指针每次往前移动一格，每次移动都会有新的一个元素进入窗口，这时条件可能就会发生改变，然后根据当前条件来决定左指针是否移动，以及移动多少格。**

## **经典题目:**

- 3. Longest Substring Without Repeating Characters (med)
- 76. Minimum Window Substring (hard)
- 239. Sliding Window Maximum (hard)
- 340. Longest Substring with At Most K Distinct Characters (hard)

Other listed by the reference

- 424 438 **480** 567 992
- 209 424 456 **480** 560 795 862 992 1100 

## **参考链接 Reference:**

- https://segmentfault.com/a/1190000019615321
- https://juejin.cn/post/6844903837447225358
- https://leetcode-cn.com/problems/permutation-in-string/solution/yong-substring-sliding-windowmo-ban-xie-de-jie-fa-/

## **模板 Template:**
### **Python**
```py
def slidingWindow(str, tar):
	## Check the constraint
	if condition: 
		return ""

	## Initialize hash table to record target change
	hashTable = {}
	for char in tar:
	
	## Initialize common variables for sliding window problem
	left = 0        # left pointer
	result = ""     # the returning result
	count = 0       # conditioning count

	## Loop over the main string by moving the right pointer
	for right in range(len(s)):
		## Update the right most char in hash table
		if s[right] in hashTable:
			
			## count up if eligibly capture a target char
				count =

		## Check the count condition
		while condition:
			## usually update left and count at this place  
			if condition:
				count =
			left =

		## Update result after while loop or within while loop
		result = 

	## return result        
	return result
```

### **JavaScript**
```js
function slidingWindow (str, tar) {
	// Check the constraint
	if (condition) {
		return "";
	}

	// Initialize hash table to record target change
	const hashTable = {};
	for (let i = 0; i < tar.length; i++) {
		hashTable[tar[i]] = ;
	}
	
	// Initialize common variables for sliding window problem
	let left = 0;       // left pointer
	let result = "";    // the returning result
	let count = 0;      // conditioning count

	// Loop over the main string by moving the right pointer
	for (let right = 0; right < str.length; right++ ){
		// Update the right most char in hash table
		if (!hashTable[str[right]]) {
			hashTable[str[right]] = ;
			// count up if eligibly capture a target char
				count = ;
		}
		// Check the count condition
		// usually update left and count at this place  
		while (condition) {
			if (condition) {
				count = ;
			}
			left = ;
		}
		// Update result after while loop or within while loop
		result = ;
	}

	// return result        
	return result;
}
```