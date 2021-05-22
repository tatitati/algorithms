# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

def solve(maze, start, goal, position):
	print([position[0], position[1]])

	# current step
	# - is goal?
	if position == goal: 
		print("GOAL")
		return True
	# - rat is in a wall?
	if maze[position[0]][position[1]] == 0: 
		print("WALL")
		return False
	# - rat is outside maze?
	if position[0] > len(maze[0]) - 1 or position[1] > len(maze) - 1: 
		print("OUT")
		return False


	# next step:
	# try right
	print("right?")
	if solve(maze, start, goal, [position[0]+1, position[1]]) == False:
		print("left?")
		# try left
		if solve(maze, start, goal, [position[0]-1, position[1]]) == False:
			print("top?")
			# try top
			if solve(maze, start, goal, [position[0], position[1]-1]) == False:
				print("bottom?")
				# try bottom
				if solve(maze, start, goal, [position[0], position[1]+1]) == False:
					return False

	# try right	
	print("end")
	return solve(maze, start, goal, [position[0]+1, position[1]])




start = [0,0]
end = [3,3]
maze = [[1, 0, 0, 0],
		[1, 1, 0, 1],
		[0, 1, 0, 0],
		[1, 1, 1, 1]]

print(solve(maze, start, end, start))