# Lista de adyacencia

# n es la cantidad de nodos
n = int(input())
g = [[] for x in range(n+1)]

# se nos dan las aristas?

m = int(input()) # leo el num de aristas
for i in range(m): 
	a, b = [int(x) for x in input().split()] # leo
	g[a].append(b) # agrego a la lista de a
	g[b].append(a) # agrego a la lista de b

for i in range(1, n+1):
	print(g[i])


vis = [False] * (n+1)

def dfs(v: int):
	print("estoy en ", v)
	vis[v] = True
	for e in g[v]:
		if not vis[e]:
			dfs(e)
	print("estoy saliendo de ", v)

dfs(1)
