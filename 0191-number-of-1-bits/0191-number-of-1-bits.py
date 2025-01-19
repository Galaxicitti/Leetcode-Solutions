class Solution:
    def hammingWeight(self, n: int) -> int:
        return [int(bit) for bit in bin(n)[2:]].count(1)
        