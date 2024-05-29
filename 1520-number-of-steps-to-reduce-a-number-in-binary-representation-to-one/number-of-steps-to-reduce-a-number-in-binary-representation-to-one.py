class Solution:
    def numSteps(self, s: str) -> int:
        check = int(s, 2)
        steps = 0
        while check > 1:
            if check % 2 == 0:
                check = check >> 1
            else:
                check += 1
            steps += 1
        return steps
        