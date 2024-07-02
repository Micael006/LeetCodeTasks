class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elems1, elems2 = [0] * 1001, [0] * 1001
        for elem in nums1:
            elems1[elem] += 1
        for elem in nums2:
            elems2[elem] += 1
        answer = []
        for i in range(len(elems1)):
            answer += [i] * min(elems1[i], elems2[i])
        return answer