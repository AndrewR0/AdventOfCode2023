
total = 0

with open("Day4/input.txt", "r") as file:
    while line := file.readline():
        game_id = line.split(":")[0]
        winning_numbers = line.rstrip().split(":")[1].split("|")[0].strip().split(" ")
        our_numbers = line.rstrip().split(":")[1].split("|")[1].strip().split(" ")
        
        # remove the empty 
        winning_numbers[:] = [x for x in winning_numbers if x != '']
        our_numbers[:] = [x for x in our_numbers if x != '']

        n = len(set(winning_numbers) & set(our_numbers))

        if n > 0:
            total += 2**(n-1)

print(total)