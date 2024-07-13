class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = dict()

        for i in range(len(nums)):
            my_dict[nums[i]] = my_dict.get(nums[i], 0) + 1
        
        buckets = []
        bucket_count = max(my_dict.values())
        for i in range(bucket_count):
            buckets.append([])
        
        for key in my_dict:
            buckets[my_dict[key] - 1].append(key)
        
        ans = []
        cur_bucket = -1
        for i in range(k):
            while len(buckets[cur_bucket]) == 0:
                cur_bucket -= 1
            ans.append(buckets[cur_bucket].pop())
        
        return ans