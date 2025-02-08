
class Solution:
    def firstBadVersion(self, n):
        L = 1
        R = n

        while L < R:
            M = (L + R) // 2
            if (isBadVersion(M)):
                R = M
            else:
                L = M + 1

        return L
