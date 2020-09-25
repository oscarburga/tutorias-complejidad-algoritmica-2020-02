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
	#visitado, padre
	vis, p= [False] * n, [-1] * n

	#ordenamiento topologico
	topo = []
	def dfs(v):
		vis[v] = True
		for e in vs[v]:
			if not vis[e]:
				dfs(e)
		topo.append(v)

	# solo nos interesa camino desde el nodo 0 hasta el n-1
	dfs(0)
	if not vis[n-1]: # si no existe ningun camino a n-1
		print("IMPOSSIBLE")
		exit()
	
	topo.reverse()
	lp = [1] * n
	for v in topo: # recorro los nodos en orden topologico
		for e in vs[v]: # trato de extender el camino actual con todos mis vecinos
			if lp[e] < lp[v] + 1: # si mi camino actual, considerando a 'e', es el mas largo
				# extiendo ese camino en 'e'
				lp[e] = lp[v] + 1
				p[e] = v
	v, path = n-1, []
	while v != -1: # reconstruimos el camino usando los padres
		path.append(v)
		v = p[v]
	path.reverse()
	return path

ans = longest_path(read_graph())
print(len(ans))
for x in ans: print(x+1, end=' \n'[x==ans[-1]])
