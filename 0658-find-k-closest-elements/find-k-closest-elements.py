class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        l -= 1
        if l >= len(arr):
            l = len(arr) - 1
        elif l < 0:
            l = 0
        r = l + 1

        answer = []
        while k > 0:
            print(l, r)
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    answer.append(arr[l])
                    l -= 1
                else:
                    answer.append(arr[r])
                    r += 1
                k -= 1
            elif l >= 0:
                answer += arr[l-k+1:l+1]
                break
            else:
                answer += arr[r:r+k]
                break
        
        answer.sort()
        return answer