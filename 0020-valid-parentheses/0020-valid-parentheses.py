from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = deque()  
        
        for i in s:
            if i in d:  
                stack.append(i)
            elif stack and d[stack[-1]] == i:  
                stack.pop()
            else:  
                return False

        return not stack  

     