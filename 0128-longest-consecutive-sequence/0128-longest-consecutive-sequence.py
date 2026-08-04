class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset=set(nums)
        longest=1

        for i in numset:
            if i - 1 not in numset:
                current=i
                count=1
                while current + 1 in numset:
                    current+=1
                    count+=1
                    longest=max(longest,count)
        return longest

        
        