import heapq as hp

inf = 10**18

n, m = map(int, input().split())
vs = [[] for i in range(n)]

for i in range(m):
	x, y, w = map(int, input().split())
	x -= 1
	y -= 1
	#Grafo dirigido
	vs[x].append((w, y)) # Par (peso, nodo)

# Hallar el camino más corto desde el nodo 1 hasta todos los demás
# Para nosotros, es el nodo 0

q = [(0, 0)] #Puedo llegar al nodo 0 con distancia 0
vis = [False] * n
d = [inf] * n #d[i]: Mejor distancia que conozco para llegar a 'i'
d[0] = 0

#La cola de prioridad contiene pares (distancia, nodo)
while len(q) > 0:
	_, v = hp.heappop(q)
	if vis[v]: continue
	vis[v] = True
	for w, e in vs[v]:
		if (not vis[e]) and d[v] + w < d[e]:
			d[e] = d[v] + w
			hp.heappush(q, (d[e], e))

		''' Prim era así:
		if (not vis[e]) and w < d[e]:
			d[e] = w
			hp.heappush((d[e], e))

		'''
for i in range(n):
	print(d[i], end=' ')
