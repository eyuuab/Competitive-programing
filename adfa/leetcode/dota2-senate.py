class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            if r_idx < d_idx:
                radiant.append(r_idx + len(senate))
            else:
                dire.append(d_idx + len(senate))

        return "Radiant" if radiant else "Dire"