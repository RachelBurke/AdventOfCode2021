#!/usr/bin/python
#  read file into array of strings
with open("./Day3Input.txt") as file:
    binary_lines = [i.strip().strip('\n') for i in file]

zeros_count_array = [0] * 12
ones_count_array = [0] * 12

#find max and min counts for each position in binary string
for line in binary_lines:
    for i in range(len(line)):
        # count 0s and 1s each column
        if line[i] == '0':
            zeros_count_array[i] += 1
        else :
            ones_count_array[i] += 1
# print(zeros_count_array) [528, 479, 515, 499, 495, 485, 488, 502, 507, 493, 504, 519]
# print(ones_count_array) [472, 521, 485, 501, 505, 515, 512, 498, 493, 507, 496, 481]

gamma = ""
epsilon = ""
for i in range(len(zeros_count_array)):
    #write to gamma and epsilon
    if ones_count_array[i] >= zeros_count_array[i]:
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)

print(str(gamma), str(epsilon)) #010111100100 101000011011
print(int(gamma,2), int(epsilon,2)) #1508 2587
print(int(gamma,2) * int(epsilon,2)) #3901196