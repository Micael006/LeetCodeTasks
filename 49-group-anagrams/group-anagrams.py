class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()

        for i in range(len(strs)):
            cur = ''.join(sorted(strs[i]))
            if cur not in my_dict:
                my_dict[cur] = []
            my_dict[cur].append(strs[i])
        
        return my_dict.values()
            