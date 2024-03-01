class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.TTL = timeToLive 
        self.tokens = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.TTL

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens.get(tokenId) and self.tokens[tokenId] > currentTime:
            self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum([1 for expiry_time in self.tokens.values() if expiry_time >currentTime])

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)