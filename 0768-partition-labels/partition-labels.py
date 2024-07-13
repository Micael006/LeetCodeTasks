class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = dict()
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = [i, i]
            else:
                my_dict[s[i]][1] = i
            
        res = sorted(my_dict.values())
        
        l, r = res[0]
        ans = []
        for i in range(1, len(res)):
            cur_l, cur_r = res[i]
            if cur_l <= r:
                l = min(cur_l, l)
                r = max(cur_r, r)
            else:
                ans.append(r - l + 1)
                l, r = cur_l, cur_r
        
        ans.append(r - l + 1)
        return ans