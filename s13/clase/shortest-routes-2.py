inf = 10**18
n, m, q = map(int, input().split())
d = [[inf for i in range(n)] for j in range(n)]

# Que pasa si me dan varias aristas entre U y V
# Necesito guardar más de una?
for i in range(m):
	x, y, w = map(int, input().split())
	x -= 1
	y -= 1
	d[x][y] = min(d[x][y], w)
	d[y][x] = min(d[y][x], w)

#La distancia  mas corta de un nodo a si mismo es 0
for i in range(n): d[i][i] = 0

for k in range(n): #fijo vertice intermedio
	for i in range(n): #fijo vertice inicio
		for j in range(n): #fijo vertice fin
			d[i][j] = min(d[i][j], d[i][k] + d[k][j])

while q > 0:
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	if d[x][y] >= inf: print(-1)
	else: print(d[x][y])
	q -= 1
