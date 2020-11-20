# https://cses.fi/problemset/task/1695/
# Aplicación clásica: Corte mínimo en un grafo
# También puede pensarse como un problema de Edge-disjoint paths
# Leer: Max-flow min-cut theorem al final de este link
# https://cp-algorithms.com/graph/edmonds_karp.html 
 
from collections import deque
 
inf = 10**9
n, m = map(int, input().split())
 
cap = [[0 for i in range(n)] for j in range(n)] 
vs = [[] for i in range(n)]
 
for i in range(m):
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	cap[x][y] = 1
	cap[y][x] = 1
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
 
# Hallar las aristas del corte mínimo
edges = []
vis = [False] * n
def dfs(v):
	vis[v] = True
	for e in vs[v]:
		if (not vis[e]) and cap[v][e] > 0:
			dfs(e)
dfs(0)
for v in range(n):
	if vis[v]:
		for e in vs[v]:
			if cap[v][e] == 0 and (not vis[e]):
				edges.append((v+1, e+1))
for e in edges:
	print(e[0], e[1])
