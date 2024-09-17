class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        helper = dict()
        for word in s1.split() + s2.split():
            helper[word] = helper.get(word, 0) + 1
        
        return [key for key in helper if helper[key] == 1]
            