# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        #后序遍历的性质，最后的数为根节点，前一部分为左子树小于根节点，后一部分为右子树大于根节点
        if len(sequence)==0:
            return False
        
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i]>root:
                break
        for j in range(i,len(sequence)):
            if sequence[j]<root:
                return False
        left = True
        if i > 0 :
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if j < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
        return right and left