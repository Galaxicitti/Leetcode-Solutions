class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        stack = deque()
        for i in s:
            print(i)
            if i in '({[':
                print(i,'a')
                stack.append(i)
            elif  len(stack)!=0:
                if d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
            else:                              
                return False
        if len(stack)==0:
            return True
        else:
            return False
      
     