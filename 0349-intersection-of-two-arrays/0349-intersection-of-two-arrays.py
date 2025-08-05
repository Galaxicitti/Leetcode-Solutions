from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        result = []
        
        for num in nums1:
            hashmap[num] = True
        
        for num in nums2:
            if num in hashmap:
                result.append(num)
                del hashmap[num]  
        
        return result
