"""
Requisitos

- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índica
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente

"""
#Lista vacia
personas_1 = []
personas_2 = []

#agregando datos
personas_1.extend(["Mathius",20,"Fisico" ])
personas_2.extend(["Maria",22, "Ingeniera"])
print("La lista 1 actualizada es: {}.".format(personas_1))
print("La lista 2 actualizada es: {}.".format(personas_2))

#Suma de edades
suma_edades = personas_1[1] + personas_2[1]
print("La suma de edades es: {}".format(suma_edades))

#Suma de ambas listas
suma_listas = personas_1 + personas_2
print("La suma de listas es: {}".format(suma_listas))

#Suma de listas de manera inversa
suma_listas.reverse()
print("La lista sumada inversa es: {}".format(suma_listas))

#eliminando las edades
suma_listas.pop(1)
suma_listas.pop(3)
print("Lista combinada sin edades: {}".format(suma_listas))

#Lista vacia
personas_2.clear()
print("Lista de la segunda persona vacía:", personas_2)