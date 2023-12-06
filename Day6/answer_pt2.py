
time = None
distance = None
total = 0
with open("Day6/input.txt", "r") as file:
    line = file.readlines()

    time = int(line[0].strip().split(":")[1].replace(" ", ""))
    distance = int(line[1].strip().split(":")[1].replace(" ", ""))

for hold_time in range(time+1):
    x = (hold_time) * (time-hold_time)
    if x > distance:
        total += 1

print(total)