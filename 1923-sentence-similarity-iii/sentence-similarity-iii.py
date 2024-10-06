class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        short_word = (sentence1 if len(sentence1) <= len(sentence2) else sentence2).split(' ')
        long_word = (sentence1 if len(sentence1) > len(sentence2) else sentence2).split(' ')

        check_index = -1
        for i in range(len(short_word)):
            if short_word[i] != long_word[i]:
                check_index = i
                break
        
        if check_index > -1:
            for i in range(len(short_word) - 1, check_index - 1, -1):
                if short_word[i] != long_word[-1 -(len(short_word) - 1) + i]:
                    return False
        
        return True