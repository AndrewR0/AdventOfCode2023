

total = 0
with open("Day1/input.txt", "r") as file:
    while line := file.readline():
        first_num = ""
        last_num = ""
        for start in range(len(line.rstrip())):
            if line[start].isnumeric():
                first_num = line[start]
                break
        for end in range(len(line.rstrip())-1, -1, -1):
            if line[end].isnumeric():
                last_num = line[end]
                break
        total += int(first_num + last_num)
print(total)
