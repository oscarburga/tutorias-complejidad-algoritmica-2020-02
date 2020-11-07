inf = 10**18
n, m = map(int, input().split())
ed = [] #edges

for i in range(m):
	x, y, w = map(int, input().split())
	ed.append((x-1, y-1, w))

# Simulo agregar un vertice que tenga una arista a todos los nodos con peso 0
d = [0] * n
p = [-1] * n
last = -1 # Guardo el último vertice modificado
for i in range(n): # N iteraciones, una de más para ver si existe ciclo negativo
	last = -1
	for u, v, w in ed: # Itero sobre todas las aristas
		if d[u] + w < d[v]: # relajo de ser necesario
			d[v] = d[u] + w
			p[v] = u
			last = v

if last == -1: #si no hice ninguna relajacion en la iteracion de más, no hay ciclo
	print("NO") #no hay ciclo negativo
else:
	x = last
	#Retroceder N veces, para garantizar que X esté dentro del ciclo
	for i in range(n): x = p[x] 
	path = [x]
	y = p[x]
	while y != x: # Retroceder en el ciclo hasta encontrar a X otra vez
		path.append(y)
		y = p[y]
	path.append(y)
	path.reverse()
	print("YES")
	for x in path: print(x+1, end=' ')
