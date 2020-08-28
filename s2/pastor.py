

def backtracking():
	### Estados: (Lado, cabra, lobo, lechuga) (todos booleanos)
	### El backtracking podría ser cíclico y no terminar nunca, por lo que necesitamos mantener
	### algo que nos diga si ya hemos visitado un estado antes.
	### Lo óptimo sería usar una mascara de bits y una matriz 2D, pero eso escapa de los temas del curso
	### Para esta ocasión, usaremos un arreglo de sets para hacer dicha verificación

	vis = [ set([]), set([]) ] ## Arreglo de 2 sets
	path = []

	def can(lado, obj): ### Funcion que me dice si puedo ir a un estado
		ret = False ### True si es invalido
		ret = ret or (obj[0] == obj[1] and lado != obj[0]) ## se queda solo lobo y cabra
		ret = ret or (obj[1] == obj[2] and lado != obj[1]) ## se queda solo cabra y col
		ret = ret or (tuple(obj) in vis[lado]) ## si ya estuve en ese estado
		return not ret ### Lo invierto para que sea True si es valido
			
	### False -> el objeto está a la izquierda del río
	### True -> el objeto está a la derecha del río

	def bt(lado = False, obj = [False, False, False]):
		if lado and (False not in obj): ### Todos están a la derecha
			return True
			
		aux = tuple(obj) ### Uso una tupla porque los sets no pueden hashear listas/arreglos mutables.

		### Opción 1: Cruzar sin llevar ningún objeto
		if can(not lado, obj):
			vis[not lado].add(aux)
			ret = bt(not lado, obj)
			if ret: ### Si encontré camino, añado el estado a la respuesta
				path.append([not lado, aux])
				return True
			vis[not lado].remove(aux)

		### Opción 2: Cruzar llevando algún objeto
		### Bug pendiente de corregir: validar que el objeto que me estoy llevando esté en el mismo lado que el pastor
		for i in range(3):
			obj[i] = not obj[i]
			aux = tuple(obj)
			if can(not lado, obj): 
				vis[not lado].add(aux)
				ret = bt(not lado, obj)
				if ret: ### Si encontré camino, añado el estado a la respuesta
					path.append([not lado, aux])
					return True
				vis[not lado].remove(aux)
			obj[i] = not obj[i]

		return False ### No encontré camino, retorno False
	return bt(), path

ans, path = backtracking()
print(ans)
path.append([False, (False, False, False)]) ### Agrego el estado inicial a la ruta
path.reverse()
for x in path: ### Imprimo la ruta
	print(x)
