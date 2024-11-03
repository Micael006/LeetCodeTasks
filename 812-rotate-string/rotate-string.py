class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        helper = s * 2
        for i in range(len(s)):
            if helper[i:i+len(s)] == goal:
                return True
        return False