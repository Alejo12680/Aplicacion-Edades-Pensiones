edades=[55, 59, 60, 55, 62, 59, 55, 63]

while True:
	print("1. Añadir edad: \n2. Añadir edad, en una posición de la lista: \n3. Longitud de la lista edades: \n4. Eliminar la última edad: \n5. Eliminar una edad: \n6. Contar edades: \n7. Personas pensionadas: \n8. Mostrar edades: \n9. Salir: ")

	menu=int(input("Ingresa opción: "))
	if menu<0 and menu>9:
		break
	elif menu==1:
		edades.append(input("Ingresa nueva edad: "))
	elif menu==2:
		edad=int(input("Ingresa nueva edad: "))
		position=int(input("En que posición lo va a insertar: "))
		if position > len(edades):
			print("Posición incorrecta")
		else:
			edades.insert(position, edad)
	elif menu==3:
		print("Longitud de la lista es: "+str(len(edades)))
	elif menu==4:
		if len(edades) > 0:
			print("El último elemento es "+edades.pop()+" y lo borramos.")
		else:
			print("La lista está vacía")
	elif menu==5:
		position=int(input("En que posición va eliminar :"))
		if position > len(edades):
			print("Posición incorrecta")
		else:
			print("El elemento que vamos a borrar es :"+str(edades.pop(position)))
	elif menu==6:
		edad=int(input("Dame la edad a buscar: "))
		print("La edad "+str(edad)+" aparece "+str(edades.count(edad))+" veces en la lista.")
	elif menu==7:
		cont=0
		for edad in edades:
			if edad >=62:
				cont+=1
		print("El número de Personas en edad de jubilación es :"+str(cont))
	elif menu==8:
		print(edades)
	elif menu==9:
		print("Salir del sistema")
		break		