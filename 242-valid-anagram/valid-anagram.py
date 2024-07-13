class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet = dict()
        for i in range(len(s)):
            alphabet[s[i]] = alphabet.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if alphabet.get(t[i], 0) == 0:
                return False
            alphabet[t[i]] -= 1
        
        return True