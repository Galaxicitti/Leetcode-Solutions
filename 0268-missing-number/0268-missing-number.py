class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actualnum = n * (n + 1) // 2 
        total = 0
        for num in nums:
            total += num  
        return actualnum - total
