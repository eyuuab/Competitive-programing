class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp  = defaultdict(int)
        ans = []
        arr1.sort()
        for i in range(len(arr1)):
            mp[arr1[i]]+=1
        for i in range(len(arr2)):
            while mp[arr2[i]]:
                ans.append(arr2[i])
                mp[arr2[i]]-=1
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                ans.append(arr1[i])
        return ans