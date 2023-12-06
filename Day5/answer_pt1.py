
mappings = []
map_to = None
mapped_list = None
found_flag = False
with open("Day5/input.txt", "r") as file:
    while line := file.readline():

        if "seeds:" in line:
            map_to = line.split(":")[1].strip().split(" ")

            for seed in map_to:
                mappings.append([0, 9999999999999, 0, 9999999999999])
            continue

        if line == "\n":
            mapped_list = []
            for i in map_to:
                for j in mappings:
                    if int(i) >= j[0] and int(i) <= j[1]:
                        x = int(i) - j[0]
                        mapped_list.append(j[2]+x)
                        found_flag = True
                        break
                if not found_flag:
                    mapped_list.append(int(i))
                found_flag = False
            mappings = []
            map_to = mapped_list

        elif ":" in line:
            continue

        else:
            dest_start = int(line.strip().split(" ")[0])
            dest_end = int(line.strip().split(" ")[0]) + int(line.strip().split(" ")[2]) - 1
            source_start = int(line.strip().split(" ")[1])
            source_end = int(line.strip().split(" ")[1]) + int(line.strip().split(" ")[2]) - 1

            mappings.append([source_start, source_end, dest_start, dest_end])


print(min(map_to))



