n = 9
sudoku = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
	sudoku[i] = [int(x) for x in input().split()]

## para que sea valido, cada numero debe aparecer una sola vez

## bool funcion(int r) {}
def check_row(r): ## O(N)
	## taken[x]: True si ya he visto el numero x en mi fila
	taken = [False] * (n+1) ## [1, 9], el 0 sobra
	for i in range(n): # for de 0 a 8
		## Estoy parado en la celda sudoku[r][i]
		x = sudoku[r][i]
		if taken[x] == True:
			return False ##La fila r es invalida
		taken[x] = True
	return True

def check_col(c): ## O(N)
	taken = [False] * (n+1)
	for i in range(n):
		## Estoy parado en la celda sudoku[i][c]
		x = sudoku[i][c]
		if taken[x] == True:
			return False
		taken[x] = True
	return True


def check_square(r, c): ###recibo la esquina superior izquierda
	## Misma idea, pero la extiendo para un cuadrado
	### Solo visito N celdas
	taken = [False] * (n+1)
	for i in range(r, r+3, 1): ## en cada paso i aumenta en 1
		for j in range(c, c+3, 1):
			x = sudoku[i][j]
			if taken[x] == True:
				return False
			taken[x] = True
	return True
	### check_square es O(N)

### Primero filas y columnas
sudoku_correcto = True
for i in range(n): ## Repeticiones O(N)
	### x and y solo es verdadero si x = 1, y = 1
	sudoku_correcto = sudoku_correcto and check_row(i) ## Costo O(N)
	sudoku_correcto = sudoku_correcto and check_col(i) ## Costo O(N)

## O(N^2) celdas que se visitan, y se procesan en O(1)
## Complejidad: O(N^2)

### Esquinas superior-izquierda de los cuadrados
### Hay N cuadrados
for i in range(0, n, 3):
	for j in range(0, n, 3):
		### Estoy llamando check_square N veces
		sudoku_correcto = sudoku_correcto and check_square(i, j)
## O(N^4) -> incorrecto
## O(N) * O(N) -> O(N^2)

if sudoku_correcto:
	print("Tu solucion es valida :)")
else:
	print("Tu solucion esta mal :(")

