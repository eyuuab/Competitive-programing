class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        mp = defaultdict(int)
        for num in nums2:
            mp[num]+=1
        nums2.sort()
        for i in range(len(nums1)):
            if nums1[i] in mp:
                return nums1[i]
        return -1
        
        # while len(nums1)>0 and len(nums2)>0:
        #     if nums1[0]==nums2[0]:
        #         return nums1[0]
        #     elif nums1[0]<nums2[0]:
        #         nums1.pop(0)
        #     else:
        #         nums2.pop(0)
        # return -1