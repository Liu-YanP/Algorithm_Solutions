class Solution:
    def StrToInt(self, s):
        # write code here
        sum =0
        numlist = ['0','1','2','3','4','5','6','7','8','9','-','+']
        if s.strip()=='':
            return 0
        isPositive = 1
        for str in s:
            if str in numlist:
                if str=='+':
                    continue
                elif str=='-':
                    isPositive=0
                    continue
                else:
                    sum = sum*10 + int(str)
            else:
                return 0
        return sum if isPositive else -sum

if __name__ == '__main__':
    s=Solution()
    print(s.StrToInt('+23'))