class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        needed_chunks = []
        answer = 0
        for i in range(len(arr)):
            needed_chunks.append([min(i, arr[i]), max(i, arr[i])])

        result = []
        while len(needed_chunks) > 0:
            cur = needed_chunks.pop()
            to_remove = set()
            for i in range(len(needed_chunks)):
                left, right = cur, needed_chunks[i]
                if left[0] > right[0]:
                    left, right = right, left
                if left[0] <= right[0] <= left[1]:
                    to_remove.add(i)
                    cur = [min(left[0], right[0]), max(left[1], right[1])]
            
            needed_chunks = [needed_chunks[i] for i in range(len(needed_chunks)) if i not in to_remove]
            
            if len(to_remove) > 0:
                needed_chunks.append(cur)
            else:
                result.append(cur)

        return len(result)        