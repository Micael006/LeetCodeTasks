class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaced = dict()
        used = set()
        for i in range(len(s)):
            if s[i] not in replaced:
                if t[i] not in used:
                    replaced[s[i]] = t[i]
                    used.add(t[i])
                else:
                    return False
            elif t[i] != replaced[s[i]]:
                return False
        return True
