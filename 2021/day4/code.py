# import numpy
# import itertools
# import more_itertools
# import os

with open(f'in.txt', 'r') as data_file:
	data = data_file.readlines()
	bingo_nums = list(map(int, data[0].strip().split(",")))
	bingo_boards = []
	for i in range(2,len(data),6):
		bingo_boards.append([list(map(int,line.strip().split())) for line in data[i:i+5]])
		
with open(f'in2.txt', 'r') as data_file:
	data = data_file.readlines()
	bingo_nums = list(map(int, data[0].strip().split(",")))
	bingo_boards = []
	for i in range(2,len(data),6):
		bingo_boards.append([list(map(int,line.strip().split())) for line in data[i:i+5]])
		
def check_if_bingo(bingo_board):
	for line in bingo_board:
		if sum(line) == -5:
			return True
	for col in zip(*bingo_board):
		if sum(col) == -5:
			return True
	return False

def find_digit(board, digit):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == digit:
				return (i,j)
	return(None,None)

def part1(bingo_nums,bingo_boards):
	
	for idx,digit in enumerate(bingo_nums):
		
		for i in range(len(bingo_boards)):
			bingo_flag = False
			x,y = find_digit(bingo_boards[i], digit)
			if x is None:
				continue
			bingo_boards[i][x][y] = -1
			bingo_flag = check_if_bingo(bingo_boards[i])
		
			if bingo_flag:
				score = 0
				for row in range(len(bingo_boards[i])):
					for col in range(len(bingo_boards[i])):
						if bingo_boards[i][row][col] != -1: 
							score += bingo_boards[i][row][col]
				return score * digit
	return None

print(part1(bingo_nums,bingo_boards))

def part2(bingo_nums,bingo_boards):
	winning_flag = [False for i in range(len(bingo_boards))]

	for idx,digit in enumerate(bingo_nums):
		for i in range(len(bingo_boards)):
			if winning_flag[i]:
				continue
			bingo_flag = False
			
			x,y = find_digit(bingo_boards[i], digit)
			if x is None:
				continue
			bingo_boards[i][x][y] = -1
			 
			bingo_flag = check_if_bingo(bingo_boards[i])
			winning_flag[i] = bingo_flag

			if bingo_flag and (sum(winning_flag) == len(winning_flag)):
				score = 0
				for row in range(len(bingo_boards[i])):
					for col in range(len(bingo_boards[i])):
						if bingo_boards[i][row][col] != -1: 
							score += bingo_boards[i][row][col]
				return score * digit
	return None

print(part2(bingo_nums,bingo_boards))
