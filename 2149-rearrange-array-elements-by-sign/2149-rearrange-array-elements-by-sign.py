class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=0
        neg=1
        arr=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]<0:
                arr[neg]=nums[i]
                neg+=2

            else:
                arr[pos]=nums[i]
                pos+=2
        return arr
        

        
        