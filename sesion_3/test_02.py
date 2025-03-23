"""Listas en python"""

"""listas -> insert(): Insertar elementos en una posicion dada y un valor"""

numbers = [40, 30.8, 100, 190, 580, 1500.45]
edad = 30
numbers.insert(1, edad)

print("Mi lista actualizada es: {}.".format(numbers))

anio = 1992

numbers.insert(4, anio)
print("Mi lista actualizada es: {}.".format(numbers))