class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        temp2=float('inf')
        for i in range(len(list1)):
            if list1[i] in list2:
                idx = list2.index(list1[i])
                temp = idx + i
                if temp == temp2:
                    ans.append(list1[i])
                elif temp < temp2:
                    temp2 = temp
                    ans = [list1[i]]
        return ans
