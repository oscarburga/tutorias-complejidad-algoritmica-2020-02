# Testeado en Eolymp https://www.e-olymp.com/en/problems/974
# Da Tiempo Límite Excedido pero da respuesta correcta
inf = 10**18

n = int(input())

#visistados, distancias finales, pesos de las aristas y funcion potencial
vis = [[False for j in range(n)] for i in range(n)]
d = [[inf for i in range(n)] for j in range(n)]
w = [[] for i in range(n)]
h = [0] * n

for i in range(n):
	w[i] = [int(x) for x in input().split()]
	
# bellman (en este caso asumo que no hay ciclos negativos)
# en el caso general, se debe verificar que no exista ningun ciclo 
# negativo o finalizar la ejecucion del algoritmo si es que existe
for i in range(n-1):
	for u in range(n):
		for v in range(n):
			if w[u][v] < inf:
				h[v] = min(h[v], h[u] + w[u][v])

# nuevos pesos de las aristas usando la funcion potencial
for u in range(n):
	for v in range(n):
		if w[u][v] < inf: 
			w[u][v] += h[u] - h[v]
			
# dijkstra (implementacion en O(N^2), sin cola de prioridad)
for src in range(n):
	d[src][src] = 0
	for i in range(n):
		v = -1
		bestd = inf
		for j in range(n):
			if (not vis[src][j]) and d[src][j] < bestd:
				bestd = d[src][j]
				v = j
		if v == -1: break
		vis[src][v] = True
		for j in range(n):
			d[src][j] = min(d[src][j], d[src][v] + w[v][j])
	#restaurar pesos
	for i in range(n):
		d[src][i] += h[i] - h[src]

for i in range(n):
	for j in range(n):
		print(d[i][j], end = ' ')
	print()

