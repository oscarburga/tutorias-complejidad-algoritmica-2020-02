import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

### Lo primero que debo hacer es leer el grafo
# N: cantidad vertices, M: cantidad aristas
n, m = [int(x) for x in input().split()]

vs = [[] for x in range(n)]
### OJO: vamos a indexar el grafo en 0, no desde 1
for i in range(m):
	x, y = [int(x) for x in input().split()]
	x -= 1
	y -= 1
	vs[x].append(y)
	vs[y].append(x)
	
def print_graph(vs):
	for i in vs:
		print(i)

#print_graph(vs)

vis = [False] * n

def dfs(v):
	vis[v] = True
	for e in vs[v]:
		if not vis[e]:
			dfs(e)

representantes = []
for i in range(n):
	if not vis[i]:
		dfs(i)
		representantes.append(i)


print(len(representantes)-1)
for i in range(len(representantes)-1):
	print(representantes[i] + 1, representantes[i+1] + 1)
