class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        my_dict = dict()
        for i in range(len(jewels)):
            my_dict[jewels[i]] = 0
        
        counter = 0
        for i in range(len(stones)):
            if stones[i] in my_dict:
                counter += 1
        return counter