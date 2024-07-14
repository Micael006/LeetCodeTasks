class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = dict()
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = [i, 0]
            my_dict[s[i]][1] += 1

        for key in my_dict:
            if my_dict[key][1] == 1:
                return my_dict[key][0]
        
        return -1 