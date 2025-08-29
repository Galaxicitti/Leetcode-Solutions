class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result^=i

        return result
        