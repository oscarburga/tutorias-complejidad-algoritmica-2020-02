'''
Problema: 
	* Oscar está llevando su curso de Redes y Protocolo de Comunicaciones.
	* A Oscar le han gustado mucho las direcciones IPv4.
	* El formato de una dirección IPv4 es el siguiente: xxx.xxx.xxx.xxx

	Oscar tiene una cadena de N dígitos y quiere saber:
	¿De cuantas formas puede Oscar separar su cadena en 4 partes no-vacías 
	para poder escribirla como si fuera una dirección IP? Imprímelas.
	
	En palabras simples: Genera todas las formas distintas de insertar 3 puntos en
	en una cadena, tal que no haya 2 puntos juntos.

	Diseñe un algoritmo de fuerza bruta cualquiera que solucione este problema.
	Diseñe un algoritmo con backtracking que solucione este problema.

'''

def fuerza_bruta(s):
	n = len(s)
	if n < 4: #Caso especial
		return 0
	### Probar todas las tripletas posibles.
	### Nota: Estoy asumiendo que coloco el punto entre las posiciones i y i+1
	ans = []
	for i in range(0, n-3):
		for j in range(i+1, n-2):
			for k in range(j+1, n-1):
				#Nota: s[L:R] considera el intervalo [L, R), abierto en R, por eso +1 en R
				t = s[0:i+1] + '.'
				t += s[i+1:j+1] + '.'
				t += s[j+1:k+1] + '.'
				t += s[k+1:n]
				ans.append(t)
	return ans

def backtracking(s):
	s = list(s) ### Convierto a lista para trabajarlo más fácil
	cur = [] ### Cadena que estoy construyendo
	ans = [] ### Respuesta
	n = len(s)
	def bt(pos, cnt): ### Voy a forzar que máximo ponga 3 puntos para que mi complejidad no vuele
		cur.append(s[pos])
		if pos == n-1:
			if cnt == 3: 
				ans.append(''.join(cur)) ### Lo único que hace es juntar todas las letras
			cur.pop(-1)
			return
		bt(pos+1, cnt) ### No poner un punto y pasar a la siguiente posicion
		if cnt < 3: ### Intentar poner un punto aquí
			cur.append('.')
			bt(pos+1, cnt+1)
			cur.pop(-1) ### pop(-1) elimina el ultimo elemento
		cur.pop(-1)
	bt(0, 0)
	return ans	


### Probar la solución

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
