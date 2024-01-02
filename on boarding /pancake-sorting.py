class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        def flip (arr, start, end):
            arr[start:end+1] = arr[start:end+1][::-1]
            print(arr)

        i, n= 0, len(arr)-1

        for i in range(len(arr)):
            max_num = len(arr)-i
            idx = arr.index(max_num)
            flip(arr,0,idx)
            flip(arr, 0,n)
          
            ans.append(idx+1)
            ans.append(n+1)
            n-=1
            i+=1
        return ans
