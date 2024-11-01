class Solution:
    def makeFancyString(self, s: str) -> str:
        cur_char, count = 'A', 0
        answer = ""
        for character in s:
            if cur_char != character:
                cur_char = character
                count = 0
            count += 1
            if count < 3:
                answer += character
        
        return answer