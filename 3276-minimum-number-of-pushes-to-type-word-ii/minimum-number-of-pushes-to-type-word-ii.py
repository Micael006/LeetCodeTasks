class Solution:
    def minimumPushes(self, word: str) -> int:
        alphabet = [0] * 26
        for sym in word:
            alphabet[ord(sym) - ord('a')] += 1
        
        for i in range(len(alphabet)):
            alphabet[i] = [alphabet[i], chr(i + ord('a'))]
        alphabet.sort(reverse=True)

        taps = dict()
        for i in range(len(alphabet)):
            taps[alphabet[i][1]] = (i // 8) + 1
        
        answer = 0
        for elem in word:
            answer += taps[elem]
        return answer
        