class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        odd_places = n //2 
        even_places = n - odd_places
        return (pow(5, even_places, mod) * pow(4, odd_places, mod)) % mod
    