class Solution:
    def maximumLength(self, s: str) -> int:
        answer = dict()
        res = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur = s[i:j + 1]
                if cur.count(cur[0]) == len(cur):
                    answer[cur] = answer.get(cur, 0) + 1
                    if answer[cur] == 3 and len(cur) > res:
                        res = len(cur)
        return res