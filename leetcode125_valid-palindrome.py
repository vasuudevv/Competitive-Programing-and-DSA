class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        t = ""
        stack = []
        x=False
        for i in s:
            if i.isalpha() or i.isnumeric():
                t = t + i
        if t == "" or len(t) == 1: return True
        print(t)
        n = len(t)
        m = n//2 
        
        for i in range(m):
            stack.append(t[i])
        print(stack) 
        m = m if n%2 == 0 else m+1
        for i in range(m,len(t)):
            
            if t[i] == stack.pop():
                x = True
            else:
                return False
        return x
            