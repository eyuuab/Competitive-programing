class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        mp = Counter(arr)
        for array in arr:
            if mp[array]>n//4:
                return array