
from math import lcm

with open("Day8/input.txt", "r") as file:
    lines = file.readlines()

    instructions = lines[0].strip()

    coord_mapping = {}
    for coords in range(2, len(lines)):
        dest = lines[coords].strip().split(" = ")[0]
        directions = lines[coords].strip().split(" = ")[1].strip("(").strip(")").split(", ")
        coord_mapping[dest] = directions

    # BRUTE FORCE SOLUTION.... DONT WORK CAUSE TAKE TOO LONG
    # current_coords = [x for x in list(coord_mapping.keys()) if x[-1] == "A"]
    # steps = 0

    # instruction_pos = 0
    # while True:
    #     tmp_coords = []
    #     for coord in current_coords:
            
    #         if instruction_pos == len(instructions):
    #             instruction_pos = 0

    #         if instructions[instruction_pos] == "R":
    #             tmp_coords.append(coord_mapping[coord][1])
    #         elif instructions[instruction_pos] == "L":
    #             tmp_coords.append(coord_mapping[coord][0])
        
    #     instruction_pos += 1
    #     steps += 1
    #     current_coords = tmp_coords
        
    #     found_zs = 0
    #     for new_coord in current_coords:
    #         if new_coord[-1] != "Z":
    #             break
    #         else:
    #             found_zs += 1
        
    #     if found_zs == len(current_coords):
    #         break
    # print(steps)


    # LCM SOLUTION
    current_coords = [x for x in list(coord_mapping.keys()) if x.endswith("A")]
    cycles = []

    for coord in current_coords:
        steps = 0
        current_coord = coord
        while not current_coord.endswith("Z"):
            for instruc in instructions:
                if instruc == "R":
                    current_coord = coord_mapping[current_coord][1]
                elif instruc == "L":
                    current_coord = coord_mapping[current_coord][0]
                steps += 1

        cycles.append(steps)
    
    print(lcm(*cycles))
