tree = '#'
num_trees = 0
currX = 0
currY = 0

with open('./input') as treemap:
    for level in treemap:
        if level[currX] == tree:
            num_trees += 1
        currX = (currX + 3) % (len(level) - 1)
        currY += 1

print(num_trees)