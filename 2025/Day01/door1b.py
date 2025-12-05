FILE_PATH = "input1a.txt"
MODULO = 100
pointer = 50
amount_of_zeros = 0

with open(FILE_PATH, "r", encoding="utf-8") as file:
    data = list(line.strip() for line in file if line != ('' or '\n'))

for item in data:
    direction = item[0]
    distance = int(item[1:])

    amount_of_zeros += int(distance / MODULO)
    distance %= MODULO

    match direction:
        case 'L':
            new_pointer = pointer - distance
            if (new_pointer <= 0 and pointer != 0):
                amount_of_zeros += 1
        case 'R':
            new_pointer = pointer + distance
            if (new_pointer > 99 and pointer != 0):
                amount_of_zeros += 1

    pointer = new_pointer % MODULO

print(f"Password to open the door is: {amount_of_zeros}")
