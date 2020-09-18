### Las 3 líneas mágicas
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

from collections import deque

n, m = [int(x) for x in input().split()]

mat = [[] for x in range(n)]
for i in range(n):
	mat[i] = list(input())

vis = [[False for i in range(m)] for j in range(n)]
q = deque()

### 4 movimientos [0, 1, 2, 3]
## mov 0: (x, y) -> (x + 1, y + 0)
## mov 1: (x, y) -> (x - 1, y + 0)
## mov 2: (x, y) -> (x + 0, y + 1)
## mov 3: (x, y) -> (x + 0, y - 1)
## en general: 
## mov i: (x, y) -> (x + dx[i], y + dy[i])
dx = [1, -1, 0, 0] 	## 1, -1, 1, -1
dy = [0, 0, 1, -1] 	## 1, -1, -1, 1



def valid(x, y):
	return (x >= 0) and (x < n) and (y >= 0) and (y < m) \
		and (mat[x][y] == '.') and (not vis[x][y])

def bfs(r, c): #row, column
	q.append((r, c))
	vis[r][c] = True
	while len(q) > 0:
		x, y = q.pop() ## x: fila, y:columna
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if valid(nx, ny):
				vis[nx][ny] = True
				q.append((nx, ny))

def dfs(x, y):
	vis[x][y] = True
	for i in range(4): 
		nx, ny = x + dx[i], y + dy[i]
		if valid(nx, ny):
			dfs(nx, ny)

	

rooms = 0
for i in range(n):
	for j in range(m):
		if mat[i][j] == '.' and (not vis[i][j]):
			rooms += 1
			bfs(i, j)
			## nota: dfs recursivo es muy lento para
			## este problema. usar BFS o 
			## DFS iterativo.

print(rooms)
