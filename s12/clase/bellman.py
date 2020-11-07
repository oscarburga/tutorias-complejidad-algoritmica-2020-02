#consideramos que guardamos las aristas como una lista
#ya no como lista de adyacencia (también se puede)

n, m = map(int, input().split())
ed = [] # Lista de aristas
for i in range(m):
	x, y, w = map(int, input().split())
	ed.append((x-1, y-1, w))

inf = 10**18
d = [inf] * n
d[0] = 0

for i in range(n-1):
	for u, v, w: 
		if d[u] < inf and d[u] + w < d[v]:
			d[v] = d[u] + w

