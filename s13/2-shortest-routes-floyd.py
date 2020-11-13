# En Python, Floyd Warshall para 500 nodos tarda 40 segundos :)
# En C++, 0.17 segundos
inf = 10**18
n, m, q = map(int, input().split())

d = [[inf for x in range(n)] for y in range(n)]

for i in range(n): d[i][i] = 0
for i in range(m):
	x, y, w = map(int, input().split())
	x -= 1
	y -= 1
	d[x][y] = min(d[x][y], w)
	d[y][x] = min(d[y][x], w)

for k in range(n):
	for i in range(n):
		for j in range(n):
			d[i][j] = min(d[i][j], d[i][k] + d[k][j])

while q > 0:
	x, y = map(int, input().split())
	res = d[x-1][y-1]
	if res >= inf: print(-1)
	else: print(res)
	q -= 1
