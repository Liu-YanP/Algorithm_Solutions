'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
	
	def twoSum1(self,nums,target):
		"""暴力解法，轮训两遍"""
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i]+nums[j] == target:
					return [i,j]

	def twoSum2(self,nums,target):
		'''用空间换时间'''
		lookup = {}#创建字典存储轮询过的数字及其索引
		for i,num in enumerate(nums):
			if target-num in lookup:
				return [lookup[target-num],i]
			else:
				lookup[num]=i


if __name__ == '__main__':
	a = Solution()
	print(a.twoSum1([2,7,11,15],13))
	print(a.twoSum2([2,7,11,15],12))
