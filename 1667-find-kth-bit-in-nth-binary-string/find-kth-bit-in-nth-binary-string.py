class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        num = "0"

        for i in range(1, n):
            prev = num
            num += "1"
            reverse_res = ""
            
            for j in range(len(prev)):
                reverse_res += str(abs(1 - int(prev[j])))
            num += reverse_res[::-1]
        
        return num[k - 1]
