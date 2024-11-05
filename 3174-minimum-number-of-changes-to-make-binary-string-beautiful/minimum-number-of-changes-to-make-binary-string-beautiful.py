class Solution:
    def minChanges(self, s: str) -> int:
        changes = len(s) % 2
        for i in range(0, len(s) - changes, 2):
            if s[i] != s[i+1]:
                changes += 1
        
        return changes