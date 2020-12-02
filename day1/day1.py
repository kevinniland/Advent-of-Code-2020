nums = []
target = 2020
flag = False
hashset = set()

with open('day1.txt', 'r') as f:
    for line in f:
        curr = line[:-1]

        nums.append(int (curr))

for i in nums:
    if i in  hashset:
        flag = True
        product = i * (target - i)
        print("Product: ", product)
    hashset.add(target - i)

    