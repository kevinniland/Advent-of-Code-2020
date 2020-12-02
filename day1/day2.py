nums = []
res = []
target = 2020
flag = False
hashset = set()

with open('day1.txt', 'r') as f:
    for line in f:
        curr = line[:-1]

        nums.append(int (curr))

for i in range(0, len(nums)-2): 
    for j in range(i + 1, len(nums)-1): 
        for k in range(j + 1, len(nums)): 
            if nums[i] + nums[j] + nums[k] == target: 
                product = nums[i] * nums[j] * nums[k]

print(product)