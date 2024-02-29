class Solution(object):
    def splitListToParts(self, root, k):
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
   
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res