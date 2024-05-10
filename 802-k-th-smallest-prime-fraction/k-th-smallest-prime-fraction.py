from fractions import Fraction
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1
        res = []

        while left <= right:
            mid = left + (right - left) / 2
            j, total, numenator, denumenator = 1, 0, 0, 0
            max_frac = 0
            for i in range(n):
                while j < n and arr[i] >= arr[j] * mid:
                    j += 1

                total += n - j

                if j < n and max_frac < arr[i] * 1.0 / arr[j]:
                    max_frac = arr[i] * 1.0 / arr[j]
                    numenator, denumenator = arr[i], arr[j]
            if total == k:
                res = [numenator, denumenator]
                break
            
            if total > k:
                right = mid
            else:
                left = mid
        return res