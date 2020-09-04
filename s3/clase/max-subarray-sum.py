### Max subarray sum

### D&C son 3 pasos principales:

### Dividir el problema
### Vencer una versión pequeña del problema
### Combinar las respuestas pequeñas para un problema mas grande

### NOTA: EL SUBARREGLO NO PUEDE SER VACÍO
def merge(a, l, mid, r):
	### Max subarray de [L+x, mid]
	sumL = a[mid]
	bestL = a[mid]
	### Empiezo de mid hacia la izquierda
	for i in range(mid-1, l-1, -1):
		sumL += a[i]
		bestL = max(sumL, bestL)
	### Max subarray de [mid+1, R-y]
	sumR = a[mid+1]
	bestR = a[mid+1]
	### Empiezo de mid+1 hacia la derecha
	for i in range(mid+2, r+1):
		sumR += a[i]
		bestR = max(sumR, bestR)
	return bestL + bestR

def solve(a, l, r):
	if l == r:
		return a[l]
	mid = (l+r)//2
	### Garantizada la mejor respuesta de [L, mid]
	left_ans = solve(a, l, mid) 
	### Garantizada la mejor respuesta de [mid+1, R]
	right_ans = solve(a, mid+1, r)
	### La unica posibilidad que no estoy considerando hasta ahora:
	### Algun subarreglo que cruce sobre el medio
	mid_ans = merge(a, l, mid, r) 
	return max(left_ans, right_ans, mid_ans)
	

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(solve(arr, 0, len(arr)-1))


### fuerza bruta:
### Fijar un punto de inicio
### luego fijar un punto de final
### actualizar la respuesta con la suma de ese rango

### el subarreglo del medio obligatoriamente es de la siguiente forma:
### [L + x, mid] + [mid+1, R-y]
