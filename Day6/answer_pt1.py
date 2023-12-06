
times = None
distances = None
with open("Day6/input.txt", "r") as file:
    while line := file.readline():

        if "Time" in line:
            times = line.strip().split(":")[1].split(" ")
            times = [int(x) for x in times if x != ""]
        elif "Distance" in line:
            distances = line.strip().split(":")[1].split(" ")
            distances = [int(x) for x in distances if x != ""]

our_distances = []
total = 1
for time in range(len(times)):
    for hold_time in range(times[time]+1):
        our_distances.append((hold_time) * (times[time]-hold_time))

    our_distances = [x for x in our_distances if x > distances[time]]
    
    total *= len(our_distances)

    our_distances = []
print(total)
