
max_combo = {"red": 12, "green": 13, "blue": 14}
total = 0

with open("Day2/input.txt", "r") as file:
    while line := file.readline():
        game_id = int(line.rstrip().split(":")[0].split(" ")[1])
        game_subset = line.rstrip().split(":")[1].split(";")

        too_many_flag = False
        for hand_pull in game_subset:
            colors = hand_pull.split(",")
            for num_color in colors:
                num = int(num_color.strip().split(" ")[0])
                color = num_color.strip().split(" ")[1]
                
                if color == "red" and num <= 12:
                    continue
                if color == "green" and num <= 13:
                    continue
                if color == "blue" and num <= 14:
                    continue
                
                too_many_flag = True
            
            if too_many_flag:
                break
        
        if not too_many_flag:
            total += game_id
print(total)

