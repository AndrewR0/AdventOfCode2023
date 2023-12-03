
nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
total = 0
with open("Day1/input.txt", "r") as file:
    while line := file.readline():
        
        first_num = ""
        lowest_num_index = 999999999
        for low_num in nums.keys():
            if low_num in line.rstrip() and line.rstrip().find(low_num) < lowest_num_index:
                lowest_num_index = line.rstrip().find(low_num)
                first_num = nums[low_num]
        for start in range(len(line.rstrip())):
            if line[start].isnumeric() and start < lowest_num_index:
                first_num = line[start]
                break

        last_num = ""
        highest_num_index = -1
        for high_num in nums.keys():
            if high_num in line.rstrip() and line.rstrip().rfind(high_num) > highest_num_index:
                highest_num_index = line.rstrip().rfind(high_num)
                last_num = nums[high_num]
        for end in range(len(line.rstrip())-1, -1, -1):
            if line[end].isnumeric() and end > highest_num_index:
                last_num = line[end]
                break

        total += int(first_num + last_num)
print(total)

# Answer = 55652