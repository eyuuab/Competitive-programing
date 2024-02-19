class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = defaultdict(int)
        stack = []
        ans =[]
        for num in nums2:
            while stack and num>stack[-1]:
                mp[stack.pop()]=num
            stack.append(num)
                
        for num in nums1:
            if num in mp:
                ans.append(mp[num])
            else:
                ans.append(-1)
        print(mp)
        return ans
