class Solution:
    def minWindow(self, s: str, t: str) -> str:
        alphabet = dict()
        for i in range(len(t)):
            alphabet[t[i]] = alphabet.get(t[i], 0) + 1
        unfound = len(alphabet)
        min_window = s + "!"
        start = 0
        for i in range(len(s)):
            print(i, unfound)
            if alphabet.get(s[i]) is not None:
                alphabet[s[i]] -= 1
                if alphabet[s[i]] == 0:
                    unfound -= 1
            if unfound == 0:
                finished = False
                while not finished:
                    if alphabet.get(s[start]) is not None:
                        alphabet[s[start]] += 1
                        if alphabet[s[start]] == 1:
                            unfound = 1
                            finished = True
                            break
                    start += 1
                #print(start, i)
                if i - start + 1 < len(min_window):
                    min_window = s[start:i+1]
                start += 1
                
        if min_window == s + "!":
            return ""
        return min_window 