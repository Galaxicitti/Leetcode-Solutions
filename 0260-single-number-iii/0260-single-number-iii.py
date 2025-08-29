class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq={}
        result =[]

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]==1:
                result.append(i)

        return result