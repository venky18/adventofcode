import numpy
import itertools
import more_itertools
import os

with open(f'in2.txt', 'r') as data_file:
    data = [int(d) for d in data_file.read().splitlines()]

#Method 1
print(sum(data[i-2] < data[i+1] for i in range(2,len(data)-1)))


#Method 2
def part1(depths):
    return sum(a < b for a, b in itertools.pairwise(depths))

def part2(depths):
    return part1(map(sum, more_itertools.triplewise(depths)))

#Method 3
data = numpy.array(data)
print(sum(data[1:]-data[0:-1]>0))
print(sum(data[3:]-data[0:-3]>0))
