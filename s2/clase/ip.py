### Test
### Se lee bien? mas grande/ mas pequeño?

## GG se destruye el formato con la letra tan grande :(
'''
Problema: 
	* Oscar está llevando su curso de Redes y Protocolo de Comunicaciones.
	* A Oscar le han gustado mucho las direcciones IPv4.
	* El formato de una dirección IPv4 es el siguiente: xxx.xxx.xxx.xxx
	Oscar tiene una cadena de N dígitos y quiere saber:
	¿De cuantas formas puede Oscar separar su cadena en 4 partes no-vacías 
	para poder escribirla como si fuera una dirección IP? Imprímelas.
	
	En palabras simples: Genera todas las formas distintas de insertar 3 puntos en
	en una cadena, tal que no haya 2 puntos juntos, y junto a cada punto hayan digitos
	a sus dos costados.
	Diseñe un algoritmo de fuerza bruta cualquiera que solucione este problema.
	Diseñe un algoritmo con backtracking que solucione este problema.
'''

def fuerza_bruta(s):
	### Algo
	n = len(s)
	### Que pasa con n < 4
	ans = []
	if n < 4:
		return ans
	for i in range(0, n-3): # O(N)
		for j in range(i+1, n-2): #O(N)
			for k in range(j+1, n-1): #O(N)
				### Partir la cadena
				### Agregar los puntos
				### s[L:R] -> devuelve el subsegmento [L: R) 
				### llamamos s[L:R+1] para compensar por el R abierto
				t = s[0:i+1] + '.'
				t += s[i+1:j+1] + '.'
				t += s[j+1:k+1] + '.'
				t += s[k+1:n]
				ans.append(t) ### Toda este bloque es O(N)
	#O(N*N*N*N) = O(N^4)
	return ans


### Un backtracking debe tener casos base
### Un backtracking debe considerar todos los movimientos validos en un estado
### Un estado es simplemente un momento/posicion en tu recursión

### Mi estado tiene que darme la información suficiente para poder saber "cómo va mi solución actual"

### En este caso yo necesito saber 2 cosas: En qué posición parado, y cuantos puntos he puesto hasta el momento
### Yo puedo verlo de esta forma:

### Mi backtracking va a ir de izquierda a derecha, y en cada posición va a considerar 2 movimientos: poner un punto, o no poner un punto
### Vamos a asumir por simplicidad que no tenemos límite de puntos

### string s = "asdf", s[2] -> d

def backtracking(s):
	## S[i:i+1]
	s = list(s)
	n = len(s)
	ans = []
	cur = []
	'''
	def f(i): 
		if i == n-1:
			### Agregar cur a ans
			### join junta todas las cadenas en cur
			cur.append(s[i])
			ans.append(''.join(cur)) ### juntar todo
			### y agregar a ans
			cur.pop(-1)
			return
		### poner un punto o no poner un punto
		### No pongo un punto
		cur.append(s[i])
		f(i+1) ## primera llamada
		### Segunda opcion: pongo un punto entre i, i+1
		cur.append('.')
		f(i+1)  ## segunda llamada, ahora con el punto
		### pop(-1) -> elimina el ultimo elem
		cur.pop(-1)  ### quito el punto
		cur.pop(-1)  ### quito la letra
		### termina mi paso recursivo
	
	### como modifico esto para que solo ponga 3 puntos?
	f(0)
	'''

	def f(i, c):
		if i == n-1:
			cur.append(s[i])
			if c == 3: ans.append(''.join(cur))
			cur.pop(-1)
			return
		cur.append(s[i])
		### Opcion 1: No pongo ningun punto
		f(i+1, c)
		### Opcion 2: Pongo un punto si es que puedo
		if c < 3: ### sin este if, la complejidad es O(n*2^(n-1))
			cur.append('.')
			f(i+1, c+1)
			### pop(-1) -> quita el ultimo elemento
			cur.pop(-1) ## quito mi punto
		cur.pop(-1)
		### termina mi paso recursivo
	f(0, 0)
	return ans


### dato curioso: la cantidad de formas se puede contar en O(1) con
### esta formula: (n-1)(n-2)(n-3)/6

import random 
def probar_solucion():
	# Dato curioso: para n = 100, existen aprox. 156mil combinaciones :)
	n = random.randint(4, 10)
	s = ''
	for i in range(n):
		s += str(random.randint(0, 9))
	ans = fuerza_bruta(s)
	print("CADENA ORIGINAL:", s)
	print("FUERZA BRUTA:", len(ans))
	for x in ans:
		print(x)
	ans = backtracking(s)
	print("\nBACKTRACKING:", len(ans))
	for x in ans:
		print(x)
	print("")


probar_solucion()

### El triple for solo recorre soluciones validas -> la formula de arriba

### el bactracking aparte tambien considera formas de poner un solo punto, formas de poner 2 puntos y formas de poner 3 puntos

### La complejidad es la misma, en la practica el triple for es mas rapido

