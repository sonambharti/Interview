"""
Given a chess board of n rows (top to bottom) and n coumns (left to right).
In each move, a knight moves either:
  1. 2 col positions and 1 row position
  2. 2 row positions and 1 column position

In other words, a move is 2 steps along one axis and 1 step along a perpendicular axis.

Given a starting position A and ending position B,
calculate the minimum no. of moves needed by the knight to move from A to B if it is possible.
If it is not possible, return -1. All moves must remain within the chess board.
"""
def isInside(x, y, N):
	if (x >= 1 and x <= N and
			y >= 1 and y <= N):
		return True
	return False

def minStepToReachTarget(n, startRow, startCol, endRow, endCol):
    startRow = startRow+1
    startCol = startCol+1
    endRow = endRow+1
    endCol = endCol+1
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    queue.append([startRow, startCol, 0])
    
    visited = [[False for i in range(n + 1)] for j in range(n + 1)]
    visited[startRow][startCol] = True
    while(len(queue) > 0):
        t = queue[0]
        queue.pop(0)
        if(t[0] == endRow and t[1] == endCol):
            return t[2]
        for i in range(8):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            
            if(isInside(x, y, n) and not visited[x][y]):
                visited[x][y] = True
                queue.append([x, y, t[2] + 1])


if _name_ == '_main_':
	n = 10
	startRow = 0
	startCol = 0
	endRow = 0
	endCol = 2

	print(minStepToReachTarget(n, startRow, startCol, endRow, endCol))
