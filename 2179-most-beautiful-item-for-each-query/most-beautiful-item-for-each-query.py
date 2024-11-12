class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        helper = dict()
        for item in items:
            price, beaty = item
            helper[price] = max(helper.get(price, 0), beaty)
        
        sorted_keys = sorted(helper.keys())
        for i in range(len(sorted_keys) - 1):
            helper[sorted_keys[i + 1]] = max(helper[sorted_keys[i + 1]], helper[sorted_keys[i]])

        answer = []
        #print(f"{sorted_keys}")

        for query in queries:
            if query < sorted_keys[0]:
                answer.append(0)
            elif query >= sorted_keys[-1]:
                answer.append(helper[sorted_keys[-1]])
            else:
                low = 0
                high = len(sorted_keys) - 1
                mid = len(sorted_keys) // 2

                while sorted_keys[mid] != query and low <= high:
                    if query > sorted_keys[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                    mid = (low + high) // 2

                #print(f"{query =}, {mid =}")
                #print(f"{sorted_keys[mid]}")

                answer.append(helper[sorted_keys[mid]])

        return answer
        
        
        

