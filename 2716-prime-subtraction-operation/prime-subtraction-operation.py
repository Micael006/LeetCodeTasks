class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = list(range(3, max(nums) + 1, 2))
        used = [False] * len(primes)
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                if not used[j] and primes[j] % primes[i] == 0:
                    used[j] = True
        
        helper = [2]
        for i in range(len(primes)):
            if not used[i]:
                helper.append(primes[i])
        
        primes = helper[:]

        def find_max_prime(num):
            for i in range(len(primes)):
                if num - primes[i] <= 0:
                    return i - 1
            return len(primes) - 1
        
        cur_index = find_max_prime(nums[0])
        if cur_index > -1:
            nums[0] -= primes[cur_index]
        
        last_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - last_num <= 0:
                return False
            cur_index = find_max_prime(nums[i] - last_num)
            if cur_index > -1:
                nums[i] -= primes[cur_index]
            last_num = nums[i]
        
        return True
        
        
