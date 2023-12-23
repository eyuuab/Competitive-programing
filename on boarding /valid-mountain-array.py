class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        cnt = 0
        if len(arr)<3:
            return False
        pick = max(arr)
        idx = arr.index(pick)
        if idx==len(arr)-1 or idx ==0:
            return False
        for i in range(idx-1):
            if arr[i]>=arr[i+1]:
                return False
        for i in range(idx,len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False
        return True