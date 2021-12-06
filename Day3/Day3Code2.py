#!/usr/bin/python
#  read file into array of strings
with open("./Day3Input.txt") as file:
    binary_lines = [i.strip().strip('\n') for i in file]

zeros_count_array = [0] * len(binary_lines[0])
ones_count_array = [0] * len(binary_lines[0])

#find max and min counts for each position in binary string
for line in binary_lines:
    for i in range(len(line)):
        # count 0s and 1s each column
        if line[i] == '0':
            zeros_count_array[i] += 1
        else :
            ones_count_array[i] += 1

oxygen = list(binary_lines)
co2 = list(binary_lines)

for i in range(len(binary_lines)):
    line = binary_lines[i]
    for j in range(len(zeros_count_array)):
        # find oxygen generator rating and CO2 scrubber rating
        if ones_count_array[j] >= zeros_count_array[j]:
            # 1 is the most common
            if line[j] == '1':
                #remove lines with 1 in position j
                if(line in co2 and len(co2) > 1):
                    co2.remove(line)
            else:
                #remove lines with 0 in position j
                if(line in oxygen and len(oxygen) > 1):
                    oxygen.remove(line);
        # 0 is the most common
        else:
            if line[j] == '0':
                #remove lines with 0 in position j
                if(line in co2 and len(co2) > 1):
                    co2.remove(line)
            else:
                #remove lines with 1 in position j
                if(line in oxygen and len(oxygen) > 1):
                    oxygen.remove(line);

print(zeros_count_array, ones_count_array)
print(oxygen)
print(co2)
print(int(oxygen[0],2) * int(co2[0], 2))