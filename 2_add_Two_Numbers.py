'''
Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
from ListNode import ListNode

class Solution(object):
	def addTwoNumbers1(self,l1,l2):
		if not l1:
			return l2
		if not l2:
			return l1

		val1,val2 = [l1.val],[l2.val]  #头结点的值
		while l1.next:
			val1.append(l1.next.val)
			l1 = l1.next
		while l2.next:
			val2.append(l2.next.val)
			l2 = l2.next

		num1 = ''.join([str(i) for i in val1[::-1]])
		num2 = ''.join([str(i) for i in val2[::-1]])

		tmp = str(int(num1)+int(num2))[::-1]  #转化为str方便倒序

		res = ListNode(int(tmp[0])) #返回的头节点
		run_res = res
		for i in range(1,len(tmp)):
			run_res.next = ListNode(int(tmp[i]))
			run_res = run_res.next
		return res  #返回头节点

	def addTwoNumbers2(self,l1,l2):
		'''递归'''
		if not l1:
			return l2
		if not l2:
			return l1

		if l1.val + l2.val<10:
			l3 = ListNode(l1.val+l2.val)
			l3.next = self.addTwoNumbers2(l1.next,l2.next)
		else:
			l3 = ListNode(l1.val+l2.val-10)
			tmp = ListNode(1)
			tmp.next = None
			l3.next = self.addTwoNumbers2(l1.next,self.addTwoNumbers2(l2.next,tmp))

		return l3


if __name__ == '__main__':
	a = Solution()
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)
	print(a.addTwoNumbers1(l1,l2))
	print(a.addTwoNumbers2(l1,l2))