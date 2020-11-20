from collections import deque

# maxima cantidad de datos que puedo enviar entre 2 computadoras

inf = 10**18
n, m = map(int, input().split())

#lista de adyacencia para el grafo residual
vs =[[] for i in range(n)] 
#matriz de capacidades para el grafo residual
cap = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
	x, y, w = map(int, input().split())
	x -= 1
	y -= 1
	cap[x][y] += w
	# grafo residual, guardo la arista en ambos sentidos
	# pero la capacidad solo en el sentido original
	vs[x].append(y)
	vs[y].append(x)


def bfs(s, t): #s: fuente, t: sumidero
	p = [-1] * n
	p[s] = -2
	# la cola guarda pares (vertice, flujo)
	# ese "flujo" es igual a la capacidad minima
	# en el camino hasta ese vertice
	q = deque([(s, inf)])
	while len(q):
		v, f = q.popleft()
		for e in vs[v]:
			if p[e] == -1 and cap[v][e] > 0:
				new_flow = min(f, cap[v][e])
				p[e] = v
				if e == t: 
					return new_flow, p
				q.append((e, new_flow))
	return 0, p

def edmondskarp(s, t):
	flow_total = 0
	while True: #mientras existan caminos aumentantes
		#manda flujo por allí
		new_flow, p = bfs(s, t)
		if new_flow == 0: return flow_total
		flow_total += new_flow
		#ahora tengo que actualizar las capacidades
		#del grafo residual
		v = t
		while v != s: #mientras que no llego a la fuente
			u = p[v] #u es el padre de v
			cap[u][v] -= new_flow
			cap[v][u] += new_flow
			v = u
		new_flow = 0

print(edmondskarp(0, n-1))
