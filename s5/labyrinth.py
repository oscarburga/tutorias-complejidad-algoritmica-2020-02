'''
Link: https://cses.fi/problemset/task/1193
 
Resumen del problema: 
Similar al Counting Rooms, se te otorga una matriz de caracteres '#'
y '.' que representan el mapa de un edificio. '#' significa que hay{
una pared en esa celda, y '.' significa que esa celda es espacio libre. 

Adicionalmente hay dos caracteres 'A' y 'B' que denotan la celda de
inicio y la celda del final, respectivamente.
 
Si no existe ningún camino para ir de 'A' a 'B', debes imprimir "NO".
Si existe algún camino, debes imprimir "YES", y hallar el que sea más
corto. Debes imprimir su longitud y la secuencia de movimientos de
dicho camino. En caso exista más de un camino más corto, puedes
imprimir cualquiera.

Los movimientos están denotados por los caracteres L, R, U, D (left,
right, up y down, respectivamente).
'''

from collections import deque
 
## Dos arreglos paralelos dx, dy para enumerar movimientos
## El movimiento i es (x + dx[i], y + dy[i])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dd = list("DURL") #para enumerar movimientos
n, m = [int(x) for x in input().split()] 

#Matriz para el mapa
mat = [[] for x in range(n)] 

start, end = (-1, -1), (-1, -1)
for i in range(n):
	mat[i] = list(input())
	for j in range(m):
		if mat[i][j] == 'A':
			start = (i, j)
		if mat[i][j] == 'B':
			end = (i, j)

# Matriz de visitados y movimientos realizados
p = [[-1 for y in range(m)] for x in range(n)] #p

p[start[0]][start[1]] = -2
q = deque([start])

def valid(r, c):
	return (r >= 0) and (r<n) and (c >= 0) and (c < m) \
		and (mat[r][c] != '#') and (p[r][c] == -1)

def reconstruct_path():
	print("YES")
	r, c  = end
	path = deque()
	while p[r][c] >= 0:
		i = p[r][c] 
		path.appendleft(dd[i])
		r -= dx[i]
		c -= dy[i]
	print(len(path))
	print(''.join(path))

		
while len(q):
	r, c = q.popleft()
	if (r, c) == end:
		reconstruct_path()
		exit()
	for i in range(4):
		nr, nc = r + dx[i], c + dy[i]
		if valid(nr, nc):
			p[nr][nc] = i
			q.append((nr, nc))

print("NO")
