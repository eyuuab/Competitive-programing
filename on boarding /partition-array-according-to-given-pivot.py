class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        large=[]
        piv=[]
        for i in nums:
            if i<pivot:
                small.append(i)
            elif i>pivot:
                large.append(i)
            else:
                piv.append(i)
        return small+piv+large