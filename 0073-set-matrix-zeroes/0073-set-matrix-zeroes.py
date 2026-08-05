class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])

        col0=1

        for i in range(m):
            if matrix[i][0]==0:
                col0=0

            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0
        if col0==0:
            for i in range(m):
                matrix[i][0]=0
            



      
        