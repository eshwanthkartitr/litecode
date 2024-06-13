class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count=0
        for i in range(len(nums1)):
            for j in range(len(nums2)): 
                if k*nums2[j]*(nums1[i] // (k*nums2[j])) == nums1[i]:
                    count+=1
        return count