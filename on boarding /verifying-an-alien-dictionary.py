class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            
            for j in range(len(first)):
                if j >= len(second):
                    return False  # One word is a prefix of the other
                
                if order.index(first[j]) > order.index(second[j]):
                    return False
                elif order.index(first[j]) < order.index(second[j]):
                    break  # Move to the next pair of words
        
        return True