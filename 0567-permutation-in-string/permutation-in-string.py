class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabet = dict()
        for elem in s1:
            alphabet[elem] = alphabet.get(elem, 0) + 1
        find_count = sum(alphabet.values())
        cur_count = find_count
        cur_alphabet = alphabet.copy()

        l = 0
        for i in range(len(s2)):
            if s2[i] not in cur_alphabet:
                cur_alphabet = alphabet.copy()
                cur_count = find_count
                l = i + 1
                continue
            
            while cur_alphabet[s2[i]] == 0:
                cur_alphabet[s2[l]] += 1
                l += 1
                cur_count += 1
            
            cur_alphabet[s2[i]] -= 1
            cur_count -= 1

            if cur_count == 0:
                break
        
        return cur_count == 0