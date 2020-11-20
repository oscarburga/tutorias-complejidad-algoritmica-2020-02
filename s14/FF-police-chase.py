# https://cses.fi/problemset/task/1695/
# Aplicación clásica: Corte mínimo en un grafo
# También puede pensarse como el problema de Edge-Disjoint paths
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

global vis
vis = [False] * n

def dfs_ff(v, f):
	vis[v] = True
	if v == n-1: return f
	for e in vs[v]:
		if (not vis[e]) and cap[v][e] > 0:
			new_flow = min(f, cap[v][e])
			sent = dfs_ff(e, new_flow)
			if sent > 0:
				cap[v][e] -= sent
				cap[e][v] += sent
				return sent
	return 0
	

def maxflow():
	global vis
	flow = 0
	while True:
		vis = [False] * n
		new_flow = dfs_ff(0, inf)
		if new_flow == 0: return flow
		flow += new_flow

print(maxflow())

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
