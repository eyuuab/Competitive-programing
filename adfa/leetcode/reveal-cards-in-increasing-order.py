
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = deque()
        deck.sort(reverse = True)
        for elem in deck:
            if result:
                prev = result.pop()
                result.appendleft(prev)
            result.appendleft(elem)
        return list(result)