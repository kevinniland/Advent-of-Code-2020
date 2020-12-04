tree = '#'
num_trees = 0
currX = 0
currY = 0
right = 1
down = 2

with open('./input') as treemap:
    for level in treemap:
        if level[currX] == tree:
            num_trees += 1
        currX = (currX + right) % (len(level) - 1)
        currY += down

print(num_trees)