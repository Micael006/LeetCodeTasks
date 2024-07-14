class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_dict = dict()
        for i in range(len(nums1)):
            if nums1[i] not in intersection_dict:
                intersection_dict[nums1[i]] = [0, 0]
            intersection_dict[nums1[i]][0] += 1
        
        for i in range(len(nums2)):
            if nums2[i] in intersection_dict:
                intersection_dict[nums2[i]][1] += 1
        
        ans = []
        for key in intersection_dict:
            ans += [key] * min(intersection_dict[key])
        return ans