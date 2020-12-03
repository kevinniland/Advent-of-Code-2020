input_file = open('./input')
lines = input_file.readlines()
input_file.close()

counter = 0
valid = 0

for line in lines:
    parts = line.split()
    policyLetter = parts[1][0]
    indexes = set(int (n) - 1 for n in parts[0].split('-'))
    password = parts[2]

    num_letters = sum(1 if p == policyLetter and i in indexes else 0 for i, p in enumerate(password))

    if (num_letters == 1):
        valid += 1

print(valid)
