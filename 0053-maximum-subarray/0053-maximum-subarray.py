class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        maxm=nums[0]

        for i in nums:
            cursum+=i
            if cursum>maxm:
                maxm=max(cursum,maxm)
            if cursum<0:
                cursum=0
        return maxm

        