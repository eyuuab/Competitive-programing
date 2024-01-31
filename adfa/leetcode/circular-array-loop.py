class Solution: 
    def circularArrayLoop(self,nums):
        def next_index(nums, index, direction):
            next = (index + nums[index]) % len(nums)
            # if the direction is not same or the next is same as current, it is not a cycle.
            if next < 0:
                next += len(nums)
            if nums[next] * direction <= 0 or next == index:
                return -1
            return next

        for i, num in enumerate(nums):
            direction = 1 if num > 0 else -1
            slow = fast = i

            while True:
                slow = next_index(nums, slow, direction)
                fast = next_index(nums, fast, direction)
                if fast != -1:
                    fast = next_index(nums, fast, direction)
                if slow == -1 or fast == -1 or slow == fast:
                    break

            if slow != -1 and slow == fast:
                return True

        return False