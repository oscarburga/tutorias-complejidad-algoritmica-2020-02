n = 9
sudoku = [[0 for x in range(n)] for y in range(n)]

### Leer sudoku
for i in range(n):
	sudoku[i] = [int(x) for x in input().split()]

### Revisar fila
def check_row(r):
	taken = [False]*10
	for i in range(n):
		x = sudoku[r][i]
		if taken[x]:
			return False
		taken[x] = True
	return True

### Revisar columna
def check_col(c):
	taken = [False]*10
	for i in range(n):
		x = sudoku[i][c]
		if taken[x]:
			return False
		taken[x] = True
	return True

### Revisar cuadrado
def check_square(r, c):
	taken = [False]*10
	for i in range(r, r+3, 1):
		for j in range(c, c+3, 1):
			x = sudoku[i][j]
			if taken[x]:
				return False
			taken[x] = True
	return True

### Revisar el tablero
correct_sudoku = True
for i in range(n):  ### Filas y columnas
	correct_sudoku = correct_sudoku and check_row(i)
	correct_sudoku = correct_sudoku and check_col(i)


for i in range(0, n, 3): ### Cuadrados de 3x3
	for j in range(0, n, 3):
		correct_sudoku = correct_sudoku and check_square(i, j)

### Imprimir resultado
if correct_sudoku:
	print("Sudoku is correct")
else:
	print("Invalid sudoku")
