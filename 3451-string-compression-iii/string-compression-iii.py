class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        answer = ""
        while i < len(word):
            cur = word[i]
            count = 1
            for pos in range(i + 1, min(i + 9, len(word))):
                if word[pos] != cur:
                    break
                count += 1
            answer += str(count) + cur
            i += count

        return answer