
total = 0

with open("Day9/input.txt", "r") as file:
    while line := file.readline():

        current_vals = line.strip().split(" ")

        last_vals = []

        while not all(int(v) == 0 for v in current_vals):
            last_vals.append(int(current_vals[-1]))
            tmp_vals = []
            for i in range(len(current_vals)-1):
                tmp_vals.append(int(current_vals[i+1]) - int(current_vals[i]))
            
            current_vals = tmp_vals
        
        next_seq = []
        last_vals = last_vals[::-1]

        for i in range(len(last_vals)):
            if i == 0:
                next_seq.append(last_vals[i])
            else:
                next_seq.append(last_vals[i] + next_seq[i-1])
        
        total += next_seq[-1]

print(total)
