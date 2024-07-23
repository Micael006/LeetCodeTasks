class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        my_d = dict()
        for num in nums:
            my_d[num] = my_d.get(num, 0) + 1

        ans = []
        for key in sorted(my_d.keys(), key=lambda x: (my_d[x], -x)):
            ans += [key] * my_d[key]
        return ans    