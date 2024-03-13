class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left , right = 0, len(letters)-1
        mid = 0
        while right>=left:
            mid = left + (right-left)//2
            print(letters[mid])
            if letters[mid]> target:
                right = mid - 1
            else:
                left = mid +1
        if mid==len(letters)-1 and letters[mid]<=target:
            return letters[0]
        if letters[mid]>target:
            return letters[mid]
        return letters[mid+1]