from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    t = input()
    nums = []
    for i in t:
        nums.append(int(i))

    cnt = 0
    prefix_sum = 0
    mp = defaultdict(int)  # Use defaultdict with int as the default factory
    mp[0]+=1
    for i in range(n):
        prefix_sum += nums[i]
        rem = (i + 1) - prefix_sum
        cnt += mp[rem]
        mp[rem] += 1
    
    print(cnt)