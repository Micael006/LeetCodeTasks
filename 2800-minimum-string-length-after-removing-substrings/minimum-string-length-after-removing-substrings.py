class Solution:
    def minLength(self, s: str) -> int:
        while True:
            ab_pos = s.find('AB')
            cd_pos = s.find('CD')
            if ab_pos != -1:
                s = s[:ab_pos] + s[ab_pos + 2:]
            elif cd_pos != -1:
                s = s[:cd_pos] + s[cd_pos + 2:]
            else:
                return len(s)