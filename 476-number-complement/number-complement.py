class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join([['0', '1'][1 - int(x)] for x in list(str(bin(num))[2:])]), 2)