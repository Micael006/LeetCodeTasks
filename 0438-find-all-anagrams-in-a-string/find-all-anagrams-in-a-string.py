class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alpha_dict = dict()

        for i in range(len(p)):
            alpha_dict[p[i]] = alpha_dict.get(p[i], 0) + 1
        
        cur_dict = alpha_dict.copy()
        max_to_find = sum(alpha_dict.values())
        cur_to_find = max_to_find

        ans = []
        l = 0
        for i in range(len(s)):
            if not s[i] in alpha_dict:
                cur_dict = alpha_dict.copy()
                cur_to_find = max_to_find
                l = i + 1
            else:
                while cur_dict[s[i]] == 0 and l < i:
                    cur_dict[s[l]] += 1
                    l += 1
                    cur_to_find += 1
                cur_dict[s[i]] -= 1
                cur_to_find -= 1
                if cur_to_find == 0:
                    ans.append(l)
                    cur_dict[s[l]] += 1
                    l += 1
                    cur_to_find += 1
        
        if cur_to_find == 0:
            ans.append(l)

        return ans