""" Operaciones comunes """
""" Operador suma """

var_1 = "7000"
var_2 = 3500
var_3 = 40.85

suma_1 = var_1 + str(var_2) #contatenacion
print(suma_1)

print("_______________________________")

nombre = "Mathius"
apellido = "Conde"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

print("_______________________________")

suma_2 = int(var_1) + var_2
print(suma_2)

print("_______________________________")

suma_3 = var_2 + var_3
print("El valor de la suma_3 es: {}".format(suma_3))

print("_______________________________")

suma_4 = var_1 + str(var_2) + str(var_3) #concatenacion
print("El valor de la suma_4 es: {}".format(suma_4))