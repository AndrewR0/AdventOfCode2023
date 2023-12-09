
total = 0

with open("Day9/input.txt", "r") as file:
    while line := file.readline():

        current_vals = line.strip().split(" ")

        last_vals = []
        first_vals = []

        while not all(int(v) == 0 for v in current_vals):
            last_vals.append(int(current_vals[-1]))
            first_vals.append(int(current_vals[0]))
            tmp_vals = []
            for i in range(len(current_vals)-1):
                tmp_vals.append(int(current_vals[i+1]) - int(current_vals[i]))
            
            current_vals = tmp_vals

            # print(first_vals, last_vals)
        

        prior_seq = []
        first_vals = first_vals[::-1]

        for i in range(len(first_vals)):
            if i == 0:
                prior_seq.append(first_vals[i])
            else:
                prior_seq.append(first_vals[i] - prior_seq[i-1])
        # print(prior_seq)
        
        total += prior_seq[-1]

print(total)
