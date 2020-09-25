import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

def read_graph():
	vs = [[] for i in range(n)]
	for i in range(m):
		x, y = map(int, input().split())
		vs[x-1].append(y-1)
	return vs


def longest_path(vs):
	#visitado, ruta a ciudad de destino, longitud del camino y siguiente nodo del camino
	vis, leh, lp, nxt = [False] * n, [False] * n, [1] * n, [-1] * n
	leh[n-1] = True #Inicialmente, solo la ciudad de destino tiene un camino a si misma
	def dfs(v):
		vis[v] = True
		for e in vs[v]:
			if not vis[e]:
				dfs(e)
			#si mi vecino 'e' tiene un camino al destino y ese camino es el más largo
			if leh[e] and lp[e] + 1 > lp[v]:
				# ahora 'v' extiende ese camino más largo
				leh[v] = True
				lp[v] = lp[e] + 1
				nxt[v] = e
	dfs(0)
	if not leh[0]: # si no existe camino a la ciudad de destino desde la primera ciudad
		print("IMPOSSIBLE")
		exit()
	v, path = 0, [] # reconstruyo el camino usando el nxt[]
	while v != -1:
		path.append(v)
		v = nxt[v]
	return path

ans = longest_path(read_graph())
print(len(ans))
for x in ans: print(x+1, end=' \n'[x==ans[-1]])
