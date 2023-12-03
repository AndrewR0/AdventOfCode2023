import numpy as np

matrix = np.loadtxt("Day3/input.txt", comments=None, dtype=str)

def found_symbol(row_index, start_index, end_index):
    
    # first row
    if row_index == 0:
        if start_index > 0:
            # left
            if matrix[row_index][start_index-1] != ".":
                return True
            
            # diagonal left down
            if not matrix[row_index+1][start_index-1].isnumeric() and matrix[row_index+1][start_index-1] != ".":
                return True
            
        # below (till end index)
        for entry in range(start_index, end_index+1):
            if not matrix[row_index+1][entry].isnumeric() and matrix[row_index+1][entry] != ".":
                return True

        if end_index < len(matrix[row_index])-1:
            # right
            if matrix[row_index][end_index+1] != ".":
                return True
            
            # diagonal right down
            if not matrix[row_index+1][end_index+1].isnumeric() and matrix[row_index+1][end_index+1] != ".":
                return True

    # last row
    if row_index == len(matrix)-1:
        if start_index > 0:
            # left
            if matrix[row_index][start_index-1] != ".":
                return True
            
            # diagonal left up
            if not matrix[row_index-1][start_index-1].isnumeric() and matrix[row_index-1][start_index-1] != ".":
                return True
            
        # above (till end index)
        for entry in range(start_index, end_index+1):
            if not matrix[row_index-1][entry].isnumeric() and matrix[row_index-1][entry] != ".":
                return True

        if end_index < len(matrix[row_index])-1:
            # right
            if matrix[row_index][end_index+1] != ".":
                return True
            
            # diagonal right up
            if not matrix[row_index-1][end_index+1].isnumeric() and matrix[row_index-1][end_index+1] != ".":
                return True

    # not first row, not first column
    if row_index > 0 and start_index > 0:
        # left
        if matrix[row_index][start_index-1] != ".":
            return True
        
        # diagonal left up
        if not matrix[row_index-1][start_index-1].isnumeric() and matrix[row_index-1][start_index-1] != ".":
            return True
            
        # above (till end index)
        for entry in range(start_index, end_index+1):
            if not matrix[row_index-1][entry].isnumeric() and matrix[row_index-1][entry] != ".":
                return True

    # not last row, not first column
    if row_index < len(matrix)-1 and start_index > 0:
        # diagonal left down
        if not matrix[row_index+1][start_index-1].isnumeric() and matrix[row_index+1][start_index-1] != ".":
            return True
        
        # below (till end index)
        for entry in range(start_index, end_index+1):
            if not matrix[row_index+1][entry].isnumeric() and matrix[row_index+1][entry] != ".":
                return True

    # not first row, not last column
    if row_index > 0 and end_index < len(matrix[row_index])-1:
        # right
        if matrix[row_index][end_index+1] != ".":
            return True
        
        # diagonal right up
        if not matrix[row_index-1][end_index+1].isnumeric() and matrix[row_index-1][end_index+1] != ".":
            return True

    # not last row, not last column
    if row_index < len(matrix)-1 and end_index < len(matrix[row_index])-1:
        # diagonal right down
        if not matrix[row_index+1][end_index+1].isnumeric() and matrix[row_index+1][end_index+1] != ".":
            return True


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
            if found_symbol(row_index, start_index, end_index):
                # print(matrix[row_index][start_index:end_index+1])
                total += int(matrix[row_index][start_index:end_index+1])
            number_found = False
            start_index = -1
            end_index = -1
print(total)
