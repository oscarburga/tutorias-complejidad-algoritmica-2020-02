import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

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


global vis
vis = [False] * n

def dfs(v, f): #vertice, capacidad minima en el camino
	global vis
	vis[v] = True
	if v == n-1: #si llegué al sumidero
		return f
	for e in vs[v]:
		if (not vis[e]) and cap[v][e] > 0:
			new_flow = min(f, cap[v][e])
			sent = dfs(e, new_flow)
			if sent > 0:
				cap[v][e] -= sent
				cap[e][v] += sent
				return sent
	#si no encontre ningun camino que llegue
	#al sumidero con flujo positivo
	#entonces retorno 0
	return 0
			
def fordfulkerson(s, t):
	global vis
	flow_total = 0
	while True: #mientras existan caminos aumentantes
		#manda flujo por allí
		vis = [False] * n
		new_flow = dfs(s, inf)
		if new_flow == 0: return flow_total
		flow_total += new_flow
		new_flow = 0

print(fordfulkerson(0, n-1))
