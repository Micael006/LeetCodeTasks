class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alphabet = dict()
        for i in range(ord('a'), ord('z') + 1):
            alphabet[chr(i)] = len(words)
        for i in range(len(words)):
            helper = [0] * 26
            for s in words[i]:
                helper[ord(s) - ord('a')] += 1
            for j in range(len(helper)):
                alphabet[chr(ord('a') + j)] = min(alphabet[chr(ord('a') + j)], helper[j])
        ans = []
        for key in alphabet:
            ans += [key] * alphabet[key]
        return ans