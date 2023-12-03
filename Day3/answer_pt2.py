import numpy as np

matrix = np.loadtxt("Day3/input.txt", comments=None, dtype=str)


gear_cache = {}

def found_symbol(row_index, start_index, end_index):
    
    # first row
    if row_index == 0:
        if start_index > 0:
            # left
            if matrix[row_index][start_index-1] == "*":
                
                if (row_index, start_index-1) in gear_cache:
                    gear_cache[(row_index, start_index-1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
                return
            
            # diagonal left down
            if matrix[row_index+1][start_index-1] == "*":
                
                if (row_index+1, start_index-1) in gear_cache:
                    gear_cache[(row_index+1, start_index-1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index+1, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
                return
            
        # below (till end index)
        for entry in range(start_index, end_index+1):
            if matrix[row_index+1][entry] == "*":
                
                if (row_index+1, entry) in gear_cache:
                    gear_cache[(row_index+1, entry)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index+1, entry)] = [matrix[row_index][start_index:end_index+1]]
                return

        if end_index < len(matrix[row_index])-1:
            # right
            if matrix[row_index][end_index+1] == "*":
                
                if (row_index, end_index+1) in gear_cache:
                    gear_cache[(row_index, end_index+1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
                return
            
            # diagonal right down
            if matrix[row_index+1][end_index+1] == "*":
                
                if (row_index+1, end_index+1) in gear_cache:
                    gear_cache[(row_index+1, end_index+1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index+1, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
                return

    # last row
    if row_index == len(matrix)-1:
        if start_index > 0:
            # left
            if matrix[row_index][start_index-1] == "*":
                
                if (row_index, start_index-1) in gear_cache:
                    gear_cache[(row_index, start_index-1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
                return
            
            # diagonal left up
            if matrix[row_index-1][start_index-1] == "*":
                
                if (row_index-1, start_index-1) in gear_cache:
                    gear_cache[(row_index-1, start_index-1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index-1, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
                return
            
        # above (till end index)
        for entry in range(start_index, end_index+1):
            if matrix[row_index-1][entry] == "*":
                
                if (row_index-1, entry) in gear_cache:
                    gear_cache[(row_index-1, entry)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index-1, entry)] = [matrix[row_index][start_index:end_index+1]]
                return

        if end_index < len(matrix[row_index])-1:
            # right
            if matrix[row_index][end_index+1] == "*":
                
                if (row_index, end_index+1) in gear_cache:
                    gear_cache[(row_index, end_index+1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
                return
            
            # diagonal right up
            if matrix[row_index-1][end_index+1] == "*":
                
                if (row_index-1, end_index+1) in gear_cache:
                    gear_cache[(row_index-1, end_index+1)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index-1, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
                return

    # not first row, not first column
    if row_index > 0 and start_index > 0:
        # left
        if matrix[row_index][start_index-1] == "*":
            
            if (row_index, start_index-1) in gear_cache:
                gear_cache[(row_index, start_index-1)].append(matrix[row_index][start_index:end_index+1])
            else:
                gear_cache[(row_index, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
            return
        
        # diagonal left up
        if matrix[row_index-1][start_index-1] == "*":
            
            if (row_index-1, start_index-1) in gear_cache:
                gear_cache[(row_index-1, start_index-1)].append(matrix[row_index][start_index:end_index+1])
            else:
                gear_cache[(row_index-1, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
            return
            
        # above (till end index)
        for entry in range(start_index, end_index+1):
            if matrix[row_index-1][entry] == "*":
                
                if (row_index-1, entry) in gear_cache:
                    gear_cache[(row_index-1, entry)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index-1, entry)] = [matrix[row_index][start_index:end_index+1]]
                return

    # not last row, not first column
    if row_index < len(matrix)-1 and start_index > 0:
        # diagonal left down
        if matrix[row_index+1][start_index-1] == "*":
            
            if (row_index+1, start_index-1) in gear_cache:
                gear_cache[(row_index+1, start_index-1)].append(matrix[row_index][start_index:end_index+1])
            else:
                gear_cache[(row_index+1, start_index-1)] = [matrix[row_index][start_index:end_index+1]]
            return
        
        # below (till end index)
        for entry in range(start_index, end_index+1):
            if matrix[row_index+1][entry] == "*":
                
                if (row_index+1, entry) in gear_cache:
                    gear_cache[(row_index+1, entry)].append(matrix[row_index][start_index:end_index+1])
                else:
                    gear_cache[(row_index+1, entry)] = [matrix[row_index][start_index:end_index+1]]
                return

    # not first row, not last column
    if row_index > 0 and end_index < len(matrix[row_index])-1:
        # right
        if matrix[row_index][end_index+1] == "*":
            
            if (row_index, end_index+1) in gear_cache:
                gear_cache[(row_index, end_index+1)].append(matrix[row_index][start_index:end_index+1])
            else:
                gear_cache[(row_index, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
            return
        
        # diagonal right up
        if matrix[row_index-1][end_index+1] == "*":
            
            if (row_index-1, end_index+1) in gear_cache:
                gear_cache[(row_index-1, end_index+1)].append(matrix[row_index][start_index:end_index+1])
            else:
                gear_cache[(row_index-1, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
            return

    # not last row, not last column
    if row_index < len(matrix)-1 and end_index < len(matrix[row_index])-1:
        # diagonal right down
        if matrix[row_index+1][end_index+1] == "*":
            
            if (row_index+1, end_index+1) in gear_cache:
                gear_cache[(row_index+1, end_index+1)].append(matrix[row_index][start_index:end_index+1])
            else:
                gear_cache[(row_index+1, end_index+1)] = [matrix[row_index][start_index:end_index+1]]
            return


total = 0

for row_index in range(len(matrix)):

    start_index = -1
    end_index = -1
    number_found = False

    for col_index in range(len(matrix[row_index])):

        if matrix[row_index][col_index].isnumeric() and start_index == -1:
            start_index = col_index
        if (start_index != -1 and col_index+1 == len(matrix[row_index])) or (start_index != -1 and not matrix[row_index][col_index+1].isnumeric()):
            end_index = col_index
            number_found = True

        if number_found:
            found_symbol(row_index, start_index, end_index)
            number_found = False
            start_index = -1
            end_index = -1

print(gear_cache)
for key in gear_cache:
    if len(gear_cache[key]) == 2:
        gear_ratio = int(gear_cache[key][0]) * int(gear_cache[key][1])
        total += gear_ratio
print(total)
