
with open("Day8/input.txt", "r") as file:
    lines = file.readlines()

    instructions = lines[0].strip()

    coord_mapping = {}
    for coords in range(2, len(lines)):
        dest = lines[coords].strip().split(" = ")[0]
        directions = lines[coords].strip().split(" = ")[1].strip("(").strip(")").split(", ")
        coord_mapping[dest] = directions

    current_coord = "AAA"
    steps = 0

    while current_coord != "ZZZ":
        for instruc in instructions:
            if instruc == "R":
                current_coord = coord_mapping[current_coord][1]
            elif instruc == "L":
                current_coord = coord_mapping[current_coord][0]
            steps += 1

            if current_coord == "ZZZ":
                break
    
    print(steps)
    