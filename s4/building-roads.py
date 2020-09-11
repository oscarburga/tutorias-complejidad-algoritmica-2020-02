'''
Link del problema: https://cses.fi/problemset/task/1666/

Resumen del enunciado: 

Se te da un grafo no-dirigido con con n vertices y m aristas. 
Calcula el mínimo número de aristas que debes agregar para que el grafo sea conexo.
Imprime una posible lista de aristas que puedes agregar para cumplir esta tarea.

Límites: N <= 10^5, M <= 2 * 10^5

Se garantiza que el grafo es simple (sin aristas multiples, etc).
'''

### Estas primeras 3 líneas son para aumentar el límite de recursión
### y el límite del tamaño del stack. 
### Es necesario para este caso porque el N y M son grandes.

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)
import random

def leer_grafo():
	n, m = [int(x) for x in input().split()]
	vs = [[] for x in range(n)]
	for i in range(m):
		a, b = [int(x) for x in input().split()]
		## Resto 1 para indexar el grafo desde 0
		a -= 1
		b -= 1
		vs[a].append(b)
		vs[b].append(a)
	return vs
		
def contar_componentes_conexas(vs):
	n = len(vs)
	vis = [False] * n
	rep = []
	def dfs(v): 
		vis[v] = True
		for e in vs[v]:
			if not vis[e]:
				dfs(e)
	### Recorro todos los nodos
	### Tiro un DFS cada vez que encuentro un nodo no visitado
	for i in range(n):
		if not vis[i]:
			#Tomo este nodo como representante de su comp.
			rep.append(i)
			dfs(i) 
	return rep

vs = leer_grafo()
rep = contar_componentes_conexas(vs)

### Imprimo el resultado
print(len(rep)-1)
for i in range(len(rep)-1):
	print(rep[i]+1, rep[i+1]+1)


