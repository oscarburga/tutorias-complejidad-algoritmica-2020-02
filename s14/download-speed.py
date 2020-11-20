#testeado en https://cses.fi/problemset/task/1694/
#Edmonds-Karp para flujo máximo
from collections import deque

inf = 10**9
n, m = map(int, input().split())

#matriz de capacidades para el grafo residual
cap = [[0 for i in range(n)] for j in range(n)] 
vs = [[] for i in range(n)]

# Si el grafo fuera muy grande como para guardar una matriz hay 2 alternativas:
# La primera (poco eficiente, pero facil de programar) es llevar un arreglo de
# hash tables (cap[v]: hash table para las capacidades que salen del vertice v)
# o un hash table de pares (cap[(u, v)] = capacidad de u a v)

# La segunda alternativa, que es mucho más eficiente pero más compleja de implementar
# es llevar la capacidad en cada arista. Para ello sería necesario guardar en cada
# arista el vertice de destino, la capacidad de la arista, el flujo que actualmente
# esta pasando por la arista y un puntero a la arista de reversa 

# De todas formas, no necesitaran estas optimizaciones muy frecuentemente

for i in range(m):
	x, y, w = map(int, input().split())
	x -= 1
	y -= 1
	cap[x][y] += w
	vs[x].append(y)
	vs[y].append(x)

def bfs(s, t): 
	q = deque([(s, inf)])
	p = [-1] * n
	p[s] = -2
	while len(q):
		v, f = q.popleft()
		for e in vs[v]:
			if p[e] == -1 and cap[v][e] > 0:
				p[e] = v
				new_flow = min(f, cap[v][e])
				if e == t: return new_flow, p
				q.append((e, new_flow))
	return 0, p

def maxflow(s, t):
	flow = 0
	while True:
		new_flow, p = bfs(s, t)
		if new_flow == 0: return flow
		v = t
		while v != s:
			u = p[v]
			cap[u][v] -= new_flow
			cap[v][u] += new_flow
			v = u
		flow += new_flow
	return flow

print(maxflow(0, n-1))

