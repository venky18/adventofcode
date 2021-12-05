# import numpy
# import itertools
# import more_itertools
# import os

with open(f'in.txt', 'r') as data_file:
	data = []
	for line in data_file.readlines():
		if len(line) > 0:
			data.append(list(map(int,line.strip().replace(' -> ',",").split(','))))

def get_coordinates(x1,y1,x2,y2):
	xy = []
	for x in range(min(x1,x2),max(x1,x2)+1):
		for y in range(min(y1,y2),max(y1,y2)+1):
			xy.append((x,y))
	return xy

def get_coordinates_diag(x1,y1,x2,y2):
	xy = [(x1,y1),(x2,y2)]
	dx = (x2-x1)//abs(x2-x1)
	dy = (y2-y1)//abs(y2-y1)
	diag_length = abs(x2-x1)

	for i in range(1, diag_length):
		xy.append((x1+(i*dx),y1+(i*dy)))
	return xy
# get_coordinates_diag(7,9,9,7)	


from collections import Counter

def part2(data):
	point_set = set()
	arr = []
	counter = 0
	for coordinates in data:
		x1,y1,x2,y2 = coordinates
		if x1 == x2 or y1 == y2:
			coords = get_coordinates(x1,y1,x2,y2)
			for coord in coords:
				arr.append(coord)

		elif abs(x1-x2) == abs(y1-y2):
			coords = get_coordinates_diag(x1,y1,x2,y2)
			for coord in coords:
				arr.append(coord)

	return (len([1 for (x,y) in Counter(arr).items() if y>1]))

print(part2(data))

