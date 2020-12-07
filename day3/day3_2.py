from functools import reduce

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_list = []
tree = '#'

input_file = open('./input')
tree_map = input_file.readlines()
input_file.close()

for right, down in slopes:
    currX, currY, counter = 0, 0, 0

    while currY < len(tree_map):
        level = tree_map[currY]

        if level[currX] == tree:
            counter += 1

        currX = (currX + right) % (len(level) - 1)
        currY += down
    tree_list.append(counter)

print(reduce(lambda a, b: a * b, tree_list))