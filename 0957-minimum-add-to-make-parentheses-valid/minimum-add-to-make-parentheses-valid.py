class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        for elem in s:
            if elem == '(':
                opened += 1
            elif elem == ')' and opened > 0:
                opened -= 1
            else:
                closed += 1
        
        return opened + closed