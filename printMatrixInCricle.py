# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        
        rows =len(matrix)
        columns = len(matrix[0])
        start = 0
        result = []
        
        while rows > start*2 and columns > start*2:
            self.printInCricle(matrix,rows,columns,start,result)
            start+=1
        return result
    
    def printInCricle(self,matrix,rows,columns,start,result):
        endX = rows-1-start
        endY = columns-1-start
        #从左往右打印一行
        for i in range(start,endX+1):
            result.append(matrix[start][i])
        #从上往下打印
        if start < endY:
            for i in range(start+1,endY+1):  #第一个数在打印第一行时已经打印，所以start+1
                result.append(matrix[i][endX])
        #从右往左打印
        if start < endX and start < endY:
            for i in range(endX-1,start-1,-1):
                result.append(matrix[endY][i])
                
        #从下往上打印
        if start<endX and start<endY-1:
            for i in range(endY-1,start,-1):
                result.append(matrix[i][start])

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(s.printMatrix(matrix))