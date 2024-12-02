class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i in range(len(words)):
            if len(words[i]) < len(searchWord):
                continue
            
            if words[i][:len(searchWord)] == searchWord:
                return i + 1
        
        return -1