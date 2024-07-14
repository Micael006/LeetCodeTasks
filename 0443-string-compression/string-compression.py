class Solution:
    def compress(self, chars: List[str]) -> int:
        def insert(arr, cur_l, cur_i, cur_pos):
            arr[cur_pos] = arr[cur_l]
            cur_pos += 1

            if cur_i - cur_l > 1:
                for char in str(cur_i - cur_l):
                    arr[cur_pos] = char
                    cur_pos += 1
            
            return arr, cur_pos    

        l = 0
        pos = 0
        for i in range(len(chars)):
            if chars[i] != chars[l]:
                chars, pos = insert(chars, l, i, pos)
                l = i

        chars, pos = insert(chars, l, len(chars), pos)

        for _ in range(pos, len(chars)):
            chars.pop()
        
        return len(chars)

        
        