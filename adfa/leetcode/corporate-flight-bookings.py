class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer=[0 for i in range(n+1)]
        for first,last,seats in bookings:
            answer[first-1]+=seats
            answer[last]-=seats
        answer = list(accumulate(answer))
        answer.pop()
        return answer