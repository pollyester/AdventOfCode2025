FILE_PATH = "input1a.txt"
MODLUO = 100
pointer = 50
amount_of_zeros = 0

with open(FILE_PATH, "r", encoding="utf-8") as file:
    data = list(line.strip() for line in file if line != ('' or '\n'))

for item in data:
    direction = item[0]
    distance = int(item[1:])

    match direction:
        case 'L':
            pointer = (pointer + distance) % MODLUO
        case 'R':
            pointer = (pointer - distance) % MODLUO

    if pointer == 0:
        amount_of_zeros += 1
    elif pointer < 0:
        pointer += MODLUO

print(f"Amount of zeros: {amount_of_zeros}")            
        