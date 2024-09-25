class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        helper = dict()
        
        for word in words:
            for i in range(1, len(word) + 1):
                cur = word[:i]
                
                if cur not in helper:
                    helper[cur] = 0
                helper[cur] += 1
        
        answer = []

        for word in words:
            points = 0

            for i in range(1, len(word) + 1):
                points += helper[word[:i]]
            
            answer.append(points)

        return answer