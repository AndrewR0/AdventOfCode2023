
total = 0

copies_cache = {}

with open("Day4/input.txt", "r") as file:
    while line := file.readline():
        game_id = line.split(":")[0].split(" ")
        game_id[:] = [x for x in game_id if x != '']

        if int(game_id[1]) not in copies_cache:
            copies_cache[int(game_id[1])] = 1

with open("Day4/input.txt", "r") as file:
    while line := file.readline():
        game_id = line.split(":")[0].split(" ")
        winning_numbers = line.rstrip().split(":")[1].split("|")[0].strip().split(" ")
        our_numbers = line.rstrip().split(":")[1].split("|")[1].strip().split(" ")
        
        # remove the empty 
        game_id[:] = [x for x in game_id if x != '']
        winning_numbers[:] = [x for x in winning_numbers if x != '']
        our_numbers[:] = [x for x in our_numbers if x != '']

        n = len(set(winning_numbers) & set(our_numbers))

        for win in range(int(game_id[1])+1, int(game_id[1])+n+1):
            copies_cache[win] += copies_cache[int(game_id[1])]

for copies in copies_cache.values():
    total += copies
    
print(total)