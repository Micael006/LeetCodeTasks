class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        my_d = dict()
        for num in nums:
            my_d[num] = my_d.get(num, 0) + 1

        ans = []
        sorted_items = list(my_d.items())
        sorted_items.sort(key=lambda tup: (tup[1], -tup[0]))
        for item in sorted_items:
            ans += [item[0]] * item[1]

        return ans    