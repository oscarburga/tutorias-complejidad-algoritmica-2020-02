### Implementación de Edmonds-Karp (flujo máximo)
### https://cses.fi/problemset/task/1696/
### Aplicación clásica: Emparejamiento Bipartito
 
n, m, k = [int(x) for x in input().split()]
 
### Número total de nodos, ID fuente, ID sumidero
maxn = n+m+2 
s = 0
t = maxn-1
 
### Crear lista de adyacencia (vs) y matriz de capacidades
### Para grafos con muchos nodos en los que la matriz sea muy grande, preferir usar diccionarios.
### Otra alternativa (más eficiente pero complicada) es guardar capacidad y flujo en cada arista.
 
vs = [[] for x in range(maxn)]
cap = [[0 for x in range(maxn)] for y in range(maxn)]
 
def add_edge(x, y):
	vs[x].append(y);
	vs[y].append(x);
	cap[x][y] = 1;
 
### Añadir aristas de la fuente a los chicos 
for i in range(1, n+1):
	add_edge(s, i)
 
### Añadir aristas de las chicas al sumidero
for i in range(n+1, n+m+1):
	add_edge(i, t)
	
### Añadir aristas entre chicos y chicas
for i in range(k):
	x, y = [int(v) for v in input().split()]
	y += n
	add_edge(x, y)
 
### Edmonds-Karp - BFS
### Como en este caso, el flujo máximo está acotado por O(N), también podría usarse un DFS.
def bfs(s, t, p):
	p[s] = -2
	q = [[s, maxn]]
	while len(q) > 0:
		v, f = q.pop(0)
		for e in vs[v]:
			if p[e] == -1 and cap[v][e] > 0:
				p[e] = v
				nf = min(f, cap[v][e])
				if e == t:
					return nf
				q.append([e, nf])
	return 0
 
### Edmonds-Karp - Loop principal
def maxflow(s, t):
	flow = 0
	while True:
		p = [-1 for x in range(maxn)]
		p[s] = -2
		new_flow = bfs(s, t, p)
		if new_flow == 0:
			break
		flow += new_flow
		### Actualizar flujo en el camino de S a T
		v = t
		while v != s:
			u = p[v]
			cap[u][v] -= new_flow
			cap[v][u] += new_flow
			v = u
	return flow
 
### Reconstruir respuesta
print(maxflow(s, t))
for i in range(1, n+1):
	for e in vs[i]:
		if e > n and e <= n+m and cap[e][i] == 1:
			print(i, e-n)
			break
