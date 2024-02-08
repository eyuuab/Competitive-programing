class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = defaultdict(lambda: [0, 0, 0, 0])

        for ind in range(len(nums)):
            freq[nums[ind]][1] += ind
            freq[nums[ind]][3] += 1

        ans =[]

        for ind in range(len(nums)):
            freq[nums[ind]][1] -= ind
            freq[nums[ind]][3] -= 1

            temp = (freq[nums[ind]][2]*ind) - freq[nums[ind]][0] +  freq[nums[ind]][1] - (freq[nums[ind]][3]*ind)
            ans.append(temp)

            freq[nums[ind]][2] += 1
            freq[nums[ind]][0] += ind
        
        return ans