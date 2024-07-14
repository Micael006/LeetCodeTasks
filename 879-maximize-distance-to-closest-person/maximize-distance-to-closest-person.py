class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l, r = 0, len(seats) - 1
        left_len, right_len = 0, 0
        between_len = 0
        for _ in range(len(seats)):
            if seats[l] == 1:
                left_len = l
                break
            l += 1

        for _ in range(len(seats)):
            if seats[r] == 1:
                right_len = len(seats) - 1 - r
                break
            r -= 1
        
        cur_l, cur_r = l, l + 1

        while cur_r <= r:
            if seats[cur_r] == 1:
                between_len = max(between_len, cur_r - cur_l)
                cur_l = cur_r
            cur_r += 1
        
        return max(left_len, right_len, between_len // 2)