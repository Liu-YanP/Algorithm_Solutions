class ListNode:
	"""docstring for Node"""
	def __init__(self,x):
		self.val = x
		self.next = None

	def __str__(self):
		tmp = [self.val]
		cur_node = self
		while cur_node.next:
			tmp.append(cur_node.next.val)
			cur_node = cur_node.next
		return ' -> '.join([str(i) for i in tmp])




		




		