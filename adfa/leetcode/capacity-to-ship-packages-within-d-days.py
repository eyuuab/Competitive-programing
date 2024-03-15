class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        
        while high >= low:
            mid = low + (high - low) //2
            day = 1
            cur = 0
            r = 0
            while r <len(weights):
                cur += weights[r]
                if cur > mid :
                    day +=1
                    cur = weights[r]
                r+=1
            if day <= days:
                high = mid - 1
            else:
                low = mid + 1
            
        return low

            
           