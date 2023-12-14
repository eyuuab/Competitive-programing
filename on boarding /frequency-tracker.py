class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.tracker2 = defaultdict(int)

    def add(self, number: int) -> None:
        if self.tracker2[self.tracker[number]] !=0:
            self.tracker2[self.tracker[number]]-=1
            if self.tracker2[self.tracker[number]] ==0:
                del self.tracker2[self.tracker[number]]
        self.tracker[number]+=1
        self.tracker2[self.tracker[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.tracker[number]!=0:
            self.tracker2[self.tracker[number]]-=1
            if self.tracker2[self.tracker[number]] ==0:
                del self.tracker2[self.tracker[number]]
       
            self.tracker[number]-=1
            self.tracker2[self.tracker[number]]+=1




    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.tracker2
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)