class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if change[0] == 0:
                    return False
                change[1] += 1
                change[0] -= 1
            else:
                if change[0] > 0 and (change[0] + 2*change[1]) >= 3:
                    if change[1] > 0:
                        change[1] -= 1
                    else:
                        change[0] -= 2
                    change[0] -= 1
                else:
                    return False
        return True