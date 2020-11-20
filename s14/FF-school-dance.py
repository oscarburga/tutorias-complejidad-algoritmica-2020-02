### Implementación de Ford-Fulkerson (flujo máximo)
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
 
### Como en este caso, el flujo máximo esta acotado por O(N), podemos usar DFS. 
### Complejidad total O(N*M) 
def dfs(v, f, p):
	if v == t:
		return f
	for e in vs[v]:
		if p[e] == -1 and cap[v][e] > 0:
			p[e] = v
			flow = dfs(e, min(f, cap[v][e]), p)
			if flow > 0:
				cap[v][e] -= flow
				cap[e][v] += flow
				return flow
	return 0
 
### Loop principal
def maxflow(s, t):
	flow = 0
	while True:
		p = [-1] * maxn
		new_flow = dfs(s, 1, p)
		if new_flow == 0:
			return flow
		flow += new_flow
			
### Reconstruir respuesta
print(maxflow(s, t))
for i in range(1, n+1):
	for e in vs[i]:
		if e > n and e <= n+m and cap[e][i] == 1:
			print(i, e-n)
			break
