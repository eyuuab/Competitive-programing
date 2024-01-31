class Solution:
    def minProcessingTime(self, ptime: List[int], tasks: List[int]) -> int:
        t =0
        res = []
        ptime.sort()
        tasks.sort(reverse = True)
        for i in range(len(ptime)):
            res.append(ptime[i]+tasks[t])
            t+=4
        return max(res)