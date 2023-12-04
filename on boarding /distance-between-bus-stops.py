class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        nums = distance
        if start>destination:
            start, destination = destination, start
        return min(sum(nums[start:destination]), (sum(nums[:start])+sum(nums[destination:])))
        