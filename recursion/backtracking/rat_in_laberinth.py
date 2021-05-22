# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
import time

currentSolutionPath = [
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]

def solve(maze, start, goal, position):
	currentSolutionPath[position[0]][position[1]] = 1
	print([position[0], position[1]])

	# current step
	# - is goal?
	if position == goal: 
		print("GOAL")	
		return True

	# - rat is outside maze?
	if position[0] > len(maze[0]) - 1 or position[0] < 0: 
		print("OUT: Y")
		return False

	if position[1] > len(maze) - 1 or position[1] < 0: 
		print("OUT: X")
		return False

	# - rat is in a wall?
	if maze[position[0]][position[1]] == 0: 
		print("WALL")
		return False

	# next step:
	print("\nright?")
	time.sleep(1)
	if currentSolutionPath[position[0]][position[1]+1] == 1 or solve(maze, start, goal, [position[0], position[1]+1]) == False: 	# try right
		print("\nleft?")
		time.sleep(1)
		if currentSolutionPath[position[0]][position[1]-1] == 1 or solve(maze, start, goal, [position[0], position[1]-1]) == False: 	# try left
			print("\ntop?")
			time.sleep(1)
			if currentSolutionPath[position[0]-1][position[1]] == 1 or solve(maze, start, goal, [position[0]-1, position[1]]) == False: # try top
				print("\nbottom?")
				time.sleep(1)				
				if currentSolutionPath[position[0]+1][position[1]] == 1 or solve(maze, start, goal, [position[0]+1, position[1]]) == False: # try bottom
					return False

	
	# # try right	
	# print("end")
	# return solve(maze, start, goal, [position[0]+1, position[1]])




start = [0,0]
end = [3,3]
maze = [[1, 0, 0, 0],
		[1, 1, 0, 1],
		[0, 1, 0, 0],
		[1, 1, 1, 1]]

solve(maze, start, end, start)