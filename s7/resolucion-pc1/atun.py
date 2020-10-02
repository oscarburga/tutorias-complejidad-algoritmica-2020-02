import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

while True:
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		quit()

	mat = [[] for i in range(n)]
	for i in range(n):
		mat[i] = list(input())

	vis = [[False for i in range(m)] for j in range(n)]
	dx = [1, -1, 0, 0, 1, 1, -1, -1]
	dy = [0, 0, 1, -1, 1, -1, 1, -1]

	def valid(r, c, i): # r: row, c: column, i: idx de movimiento
		x = r + dx[i]
		y = c + dy[i]
		return x >= 0 and x < n and y >= 0 and y < m and \
			(not vis[x][y]) and (mat[x][y] != '#')

	def dfs(r, c):
		vis[r][c] = True
		for i in range(8):
			if valid(r, c, i):
				dfs(r + dx[i], c + dy[i])

	cnt = 0
	for i in range(n):
		for j in range(m):
			if not vis[i][j] and mat[i][j] == 'F':
				dfs(i, j)
				cnt += 1

	print(cnt)
