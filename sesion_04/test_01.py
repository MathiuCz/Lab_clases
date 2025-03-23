"""Diccionarios en python"""

"""Los nombres de los keys (llaves) van a ir escritos siempre
en minusculas y sin tildes (por convecion o po rbuenas practicas)"""

var_1 = {"nombre": "Mathius", "edad": 20, "promedio": 14.5}
print("Mi diccionario tiene el siguiente contenido {}".format(var_1))

"""Agregamos elementos a un nuevo diccionario"""
var_1["distrito"] = "La Victoria"
var_1["nombre"] = "José"
var_1["habilitado"] = True

print(var_1)