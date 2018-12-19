class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = n
        tmp = ans and  self.Sum_Solution(n-1)
        ans+=tmp
        return ans


if __name__ == '__main__':
	s=Solution()
	print(s.Sum_Solution(100))