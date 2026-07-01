class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        for _ in range(1,numRows):
            temp = [1] * (len(res[-1]) + 1)
            for i in range(1,len(temp)-1):
                temp[i] = res[-1][i-1] + res[-1][i]
            res.append(temp)
        return res
        