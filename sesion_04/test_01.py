"""Diccionarios en python"""

"""Los nombres de los keys (llaves) van a ir escritos siempre
en minusculas y sin tildes (por convecion o po rbuenas practicas)"""

var_1 = {"nombre": "Mathius", "edad": 20, "promedio": 14.5}
print("Mi diccionario tiene el siguiente contenido {}".format(var_1))

"""Agregamos elementos a un nuevo diccionario"""
var_1["distrito"] = "La Victoria"
var_1["nombre"] = "José"
var_1["habilitado"] = True

#Solo valores
var_values = var_1.values()
print(var_values)
print(var_1)

#obtener los valores en especifico de un key
solo_nombre = var_1.get("nombre")
#Tambien funciona d1["nombre"]
print(solo_nombre)