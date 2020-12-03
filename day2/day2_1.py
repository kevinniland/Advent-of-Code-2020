input_file = open('./input')
lines = input_file.readlines()
input_file.close()

counter = 0
valid = 0

for line in lines:
    parts = line.split()
    policyLetter = parts[1][0]
    min, max = [int (n) for n in parts[0].split('-')]
    password = parts[2]

    num_letters = sum(1 if p == policyLetter else 0 for p in password)

    if min <= num_letters <= max:
        valid += 1

print(valid)