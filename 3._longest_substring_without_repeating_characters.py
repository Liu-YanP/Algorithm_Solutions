'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
	Input: "abcabcbb"
	Output: 3 
	Explanation: The answer is "abc", with the length of 3. 
Example 2:
	Input: "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.
Example 3:
	Input: "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3. 
	 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
	"""
	l:代表目前子串的最大长度
	start：是这轮末重复子串的首字母的index
	maps：放置每个字符串的index，如果maps.get(s[i],-1)大于等于start
	这说明字符串重复。需要重置l和start
	"""
	def lengthOfLongestSubstring1(self,s):
		l,start,n = 0,0,len(s)
		maps = {}
		for i in range(n):
			start = max(start,maps.get(s[i],-1)+1)
			l = max(l,i - start+1)
			maps[s[i]] = i
		return l

#滑动窗口
	def lengthOfLongestSubstring2(self,s):
		lookup = {}
		start,end,counter,length = 0,0,0,0
		while end<len(s):
			lookup[s[end]] = lookup.get(s[end],0) + 1
			if lookup[s[end]]==1:
				counter += 1
			end +=1
			while start<end and counter < end-start:
				lookup[s[start]] -= 1
				if lookup[s[start]]==0:
					counter -=1
				start +=1
			length = max(length,end-start)
		return length

if __name__ == '__main__':
	s = 'abcebcbb'
	solu = Solution()
	print(solu.lengthOfLongestSubstring1(s))
	print(solu.lengthOfLongestSubstring2(s))