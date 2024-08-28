class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=lambda x: sorted(x))
        answer = []
        helper = [strs[0]]
        for i in range(1, len(strs)):
            if sorted(strs[i]) != sorted(helper[-1]):
                answer.append(helper)
                helper = []
            helper.append(strs[i])
        
        answer.append(helper)

        return answer