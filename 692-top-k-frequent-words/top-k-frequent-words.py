class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        my_dict = dict()
        for word in words:
            my_dict[word] = my_dict.get(word, 0) + 1
        
        helper = dict()
        for key in my_dict:
            helper[my_dict[key]] = helper.get(my_dict[key], []) + [key]
        
        for key in helper:
            helper[key].sort()
        
        ans = []
        s_keys = sorted(helper.keys())[::-1]
        cur_key = 0
        cur_word = 0
        for i in range(k):
            ans.append(helper[s_keys[cur_key]][cur_word])
            cur_word += 1
            if cur_word == len(helper[s_keys[cur_key]]):
                cur_key += 1
                cur_word = 0

        return ans


        
        return ans
