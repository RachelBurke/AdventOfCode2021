#!/usr/bin/python
#  read file into array of strings
with open("./Day3Input.txt") as file:
    binary_lines = [i.strip().strip('\n') for i in file]

#find max and min counts for each position in binary string
def count_bits(lines):
    zeros_count = [0] * len(binary_lines[0])
    ones_count = [0] * len(binary_lines[0])
    for line in lines:
        for i in range(len(line)):
            # count 0s and 1s each column
            if line[i] == '0':
                zeros_count[i] += 1
            else :
                ones_count[i] += 1
    return zeros_count, ones_count

# find oxygen generator rating and CO2 scrubber rating
oxygen = list(binary_lines) # most common
co2 = list(binary_lines) # least common

for i in range(len(oxygen[0])):
    zeros, ones = count_bits(binary_lines)
    for line in binary_lines:
        # if there are an equal number of bits
        if zeros[i] == ones[i]:
            #remove 0 bits from oxygen
            if(line[i] == "0" and line in oxygen and len(oxygen) > 1):
                oxygen.remove(line)
        #if there are more 0 bits than 1 bits
        elif zeros[i] > ones[i]:
            #remove 1 bits from oxygen
            if(line[i] == "1" and line in oxygen and len(oxygen) > 1):
                oxygen.remove(line)
        #if there are more 1 bits than 0 bits
        elif ones[i] > zeros[i]:
            #remove 0 bits from oxygen
            if(line[i] == "0" and line in oxygen and len(oxygen) > 1):
                oxygen.remove(line)

for i in range(len(co2[0])):
    zeros, ones = count_bits(binary_lines)
    for line in binary_lines:
        # if there are an equal number of bits
        if zeros[i] == ones[i]:
            #remove 1 bits from co2
            if(line[i] == "1" and line in co2 and len(co2) > 1):
                co2.remove(line)
        #if there are more 0 bits than 1 bits
        elif zeros[i] > ones[i]:
            #remove 0 bits from co2
            if(line[i] == "0" and line in co2 and len(co2) > 1):
                co2.remove(line)
        #if there are more 1 bits than 0 bits
        elif ones[i] > zeros[i]:
            #remove 1 bits from co2
            if(line[i] == "1" and line in co2 and len(co2) > 1):
                co2.remove(line)

print(oxygen, co2) #['010111100100'] ['101000010001']
print(int(oxygen[0],2), int(co2[0], 2)) #1508 2577
print(int(oxygen[0],2) * int(co2[0], 2)) #3886116