import heapq as hp

#nodos, aristas
n, m = map(int, input().split())
#la lista de adj ahora guarda pares (nodo, peso)
vs = [[] for i in range(n)]

for i in range(m):
	x, y, w = map(int, input().split())
	vs[x].append((y, w))
	vs[y].append((x, w))

inf = 10**9

vis = [False] * n # procesados
q = [(0, 0)] # Empiezo desde el nodo 0
# Python por defecto ordena lexicograficamente
# (x, y), primero se ordena por x, se rompen empates por y
# Atencion: En 'q' se guarda como (peso, nodo)

# Costo con el que llegué a cada nodo
c = [inf] * n
c[0] = 0
# 'c' guarda el mejor peso que conozco para llegar a cada nodo

# Las operaciones del heap son todas O(logn)

peso_mst = 0
while len(q) > 0:
	# recordar: q tiene pares (peso, nodo)
	_, v = hp.heappop(q) #Extraer minimo en O(logn)
	
	#Si ya he procesdo este nodo antes, me lo salto #extraer minimo
	if vis[v]: continue 
	# continue salta de frente a la sgte iteracion del while
	vis[v] = True
	peso_mst += c[v] # Sumo el costo con el que llegué a la rpta final
	for e, w in vs[v]: #w: weight
		if (not vis[e]) and w < c[e]: 
			c[e] = w #actualizo mejor peso
			hp.heappush(q, (w, e)) #meto a la cola

print(peso_mst)
