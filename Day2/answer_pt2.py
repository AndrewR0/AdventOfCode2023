
total = 0

with open("Day2/input.txt", "r") as file:
    while line := file.readline():
        game_id = int(line.rstrip().split(":")[0].split(" ")[1])
        game_subset = line.rstrip().split(":")[1].replace("; ", ", ").strip().split(", ")

        print(game_subset)

        cache = {"red": 0, "green": 0, "blue": 0}

        for num_color in game_subset:
            num = int(num_color.split(" ")[0])
            color = num_color.split(" ")[1]

            if num > cache[color]:
                cache[color] = num
        
        total += (cache["red"] * cache["blue"]* cache["green"])

print(total)