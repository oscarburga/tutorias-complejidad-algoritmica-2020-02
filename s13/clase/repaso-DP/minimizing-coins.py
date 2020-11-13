'''
Sobre el BUG que tuvimos en la clase:
Resulta que el Runtime Error que teníamos era por límite de memoria excedido.
Una matriz de 100 * (10^6) requiere 10^8 celdas de 8 bytes cada una, 
lo cual es 800 megabytes aprox. En clase, cuando calcule el límite de memoria.
Tuve un typo al hacer los cálculos y puse (8 * 10**7) / 10**6, cuando debía 
ser (8 * 10**8) / 10**6.

Es interesante que de Runtime Error en vez de Memory Limit Exceeded.

Por lo tanto, para optimizar la memoria, podemos hacer un truco parecido al que
se utiliza en Floyd Warshall: Notar que solo se necesita el dp[i-1] para 
construir dp[i], por lo que podemos reducir el uso de memoria a O(X). La 
complejidad temporal se mantiene en O(N*X)

Nota: Igual hay 1 caso que da TLE en Python, también les dejo mi solución
en C++ para que la revisen.
'''
#minima cantidad de monedas para sumar X
#las monedas ya tienen denominacion fisica
#O(N*X)

'''
dp[i][x]: minima cantidad de monedas para sumar X 
          podiendo utilizar solo las primeras i monedas

dp[k][0]: 0

estoy considerando tomar una nueva moneda:
Para la iésima moneda, tengo 2 opciones: 
1) No necesito esta moneda para obtener la respuesta óptima
2) Necesito esta moneda para obtener la respuesta óptima

opcion 1: dp[i-1][x]
opcion 2: tomar la mejor opcion para llegar a una suma SIN 
	  esta moneda, y agregar esta moneda: dp[i][x-a[i]] + 1
dp[i][x]: min(dp[i-1][x], dp[i][x-a[i]]
'''

inf = 10**18
n, X = map(int, input().split())

a = [int(k) for k in input().split()]
dp = [inf for i in range(X+1)] 
# elimino una dimension de mi DP, mismo truco que FloydWarshall

dp[0] = 0
for i in range(1, n+1): #itero sobre las monedas
	for s in range(X+1): #itero sobre la suma
		if s >= a[i-1]: 
			dp[s] = min(dp[s], dp[s-a[i-1]] + 1)

if dp[X] >= inf: print(-1)
else: print(dp[X])
