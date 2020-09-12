### Este problema queda pendiente para el próximo taller
'''
Link: https://cses.fi/problemset/task/1192

Resumen del problema: 
Se te otorga una matriz de caracteres '#' y '.' que representan el mapa
de un edificio. '#' significa que hay una pared en esa celda, y '.' 
significa que esa celda es espacio libre. 

Cuenta la cantidad de habitaciones en el edificio.


Observación: Debo contar componentes conexas en la matriz.
¿Cómo puedo trabajar esto? ¿Construyo un grafo a partir de la matriz?

En cada celda puedo moverme en las direcciones ><^v
Formalmente, de (x, y) puedo ir a (x+1, y), (x-1, y), (x, y+1), (x, y-1)

Nota: Por desgracia, en este problema probablemente obtengamos 'Tiempo
límite excedido' usando Python. La misma solución en C++ pasa en 0.06
segundos como máximo.
'''

### Las 3 líneas mágicas
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

def solve():
	## Dos arreglos paralelos dx, dy para enumerar movimientos
	## El movimiento i es (x + dx[i], y + dy[i])
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	n, m = [int(x) for x in input().split()] 
	#Matriz para el mapa
	mat = [[] for x in range(n)] 
	for i in range(n):
		mat[i] = list(input())
	# Matriz de visitados
	vis = [[False for y in range(m)] for x in range(n)]

	def valid(r, c):
		ret = (r >= 0) and (r < n)
		ret = ret and (c >= 0) and (c < m)
		if not ret: return False ### Se sale de los límites de mi matriz
		ret = ret and (mat[r][c] == '.') and (not vis[r][c])
		return ret
	
	def dfs(r, c): #r: row, c: column
		vis[r][c] = True
		for i in range(4):
			if valid(r + dx[i], c + dy[i]):
				dfs(r + dx[i], c + dy[i])

	rooms = 0
	for i in range(n):
		for j in range(m):
			if (mat[i][j] == '.') and (not vis[i][j]):
				rooms += 1
				dfs(i, j)
	return rooms
				
print(solve())
