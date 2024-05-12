class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        answer = 0
        while l <= r:
            if lmax <= rmax:
                lmax = max(lmax, height[l])
                answer += max(0, lmax - height[l])
                l += 1
            else:
                rmax = max(rmax, height[r])
                answer += max(0, rmax - height[r])
                r -= 1
        return answer