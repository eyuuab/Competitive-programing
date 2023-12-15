class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even=0
        for num in nums:
            if num%2:
                continue
            else:
                even+=num

        for querie in queries:

            val,idx = querie
            preval = nums[idx]

            if preval%2==0:
                even-=preval
            nums[idx] = preval+val

            if nums[idx]%2==0:
                even+=nums[idx]
            ans.append(even)
            
        return ans

        #     if val%2==0:
        #         if val<0 or nums[querie[1]]%2==0:
        #             even-=nums[querie[1]]
        #         even+=val
        #         nums[querie[1]]=val
        #     else:
        #         even-=nums[querie[1]]
        #         nums[querie[1]] = val
        #     ans.append(even)
        
        #     print(even)
        #     print(nums)
        # if ans==[-1]:
        #     ans=[0]
