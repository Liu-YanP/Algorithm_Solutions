# -*- coding:utf-8 -*-
'''
构建一个栈数据结构，并实现查找最小元素的时间复杂度为O(1)
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, node):
        self.stack.append(node)
        if self.minstack==[] or node<self.min():
            self.minstack.append(node)  #如果比最小的小，则存入minstack
        else:
            tmp = self.min()       #否则继续将最小的值存入minstack
            self.minstack.append(tmp)
            
    def pop(self):
        if self.stack == None and self.minstack==None:
            return None
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minstack[-1]
