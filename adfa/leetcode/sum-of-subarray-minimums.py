class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        stack=[(0,-1)]
        pref, suf = [],[]

        for i in range(len(nums)):
            if nums[i]>stack[-1][0]:
               
                diff = i- stack[-1][1]
                pref.append(diff)
                stack.append((nums[i],i))
            else:
                while stack[-1][0]>=nums[i]:
                    stack.pop()
               
                diff = i- stack[-1][1]
                pref.append(diff)
                stack.append((nums[i],i))

        stack=[(0,len(nums))]
       
        for i in range(len(nums)-1,-1,-1):

            if nums[i]>stack[-1][0]:
                diff = stack[-1][1]-i
                suf.append(diff)
                stack.append((nums[i],i))
            else:
                while stack[-1][0]>nums[i]:
                    stack.pop()
                diff = stack[-1][1]-i
                suf.append(diff)
                stack.append( (nums[i],i) )
        suf = suf[::-1]
        meti = 0
        for i in range(len(pref)):
            meti+= pref[i] * suf[i] * nums[i]

        return meti %(10**9 + 7 )
    