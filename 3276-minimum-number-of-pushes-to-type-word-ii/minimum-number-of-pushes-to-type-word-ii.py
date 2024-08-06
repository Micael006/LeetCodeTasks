class Solution:
    def minimumPushes(self, word: str) -> int:
        alphabet = [0] * 26
        for sym in word:
            alphabet[ord(sym) - ord('a')] += 1
        alphabet.sort(reverse=True)

        answer = 0
        for i in range(len(alphabet)):
            answer += alphabet[i] * ((i // 8) + 1)
        
        return answer
        