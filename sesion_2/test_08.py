""" Conversion de datos """""

"""Creacion de variables"""

var_str = "20250"
nombre = "Joaquin"
modulo = 1
prom = 17.8

#Conversion de string a entero
var_int = int(var_str)
print(type(var_int))
print(var_int)

#Conversion de entero a string
var_mod = str(modulo)
print(type(var_mod))
print(var_mod)

#Conversion de string a entero (no será posible realizar la conversión)
# var_nom = int(nombre)
#print(type(var_nom))

#Conversion de flotante a entero
var_prom = int(prom)
print(type(var_prom))
print(var_prom)