# import numpy
# import itertools
# import more_itertools
# import os

with open(f'in.txt', 'r') as data_file:
    # data = [[k] for ele in data_file.readlines() for k in ele.split(' ')]
     part1data = [list(map(str.strip,ele.split(' '))) for ele in data_file.readlines()]
    	
with open(f'in2.txt', 'r') as data_file:
    # data = [[k] for ele in data_file.readlines() for k in ele.split(' ')]
     part2data = [list(map(str.strip,ele.split(' '))) for ele in data_file.readlines()]

def part11(data):
	depth = 0
	position  = 0
	print(data)
	for ele in data:
		print(ele[0], ele[1])
		
		if ele[0] == 'forward':
			position += int(ele[1])
		
		if ele[0] == 'up':
			depth -= int(ele[1])
		
		if ele[0] == 'down':
			depth += int(ele[1])

	print(depth*position)



def part2(data):
	depth = 0
	position  = 0
	aim = 0
	print(data)
	for ele in data:
		val = int(ele[1])
		if ele[0] == 'down':
			aim += val
		
		if ele[0] == 'up':
			aim -= val		
		
		if ele[0] == 'forward':
			position += val
			depth += aim*val
	print(depth*position)

part2(part2data)