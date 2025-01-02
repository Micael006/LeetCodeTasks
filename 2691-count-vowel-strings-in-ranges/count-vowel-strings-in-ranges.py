class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(len(words)):
            prefix.append(prefix[-1] + int((words[i][0] in vowels) and (words[i][-1] in vowels)))
        
        answer = []
        for start, end in queries:
            answer.append(prefix[end + 1] - prefix[start])
        
        return answer