"""
Requisito

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string
con contenido solamente numérico y 1 variable boolean

2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(realizar conversiones si es necesario)

3. Obtener y mostar la suma de las 2 variables enteras más la variable string numérica y la
variable flotante

4. Obtener y mostrar el módulo de las variables enteras: %

5. Obtener y mostarar el resultado entero o la parte entera de las 2 variables int: //

6. Obtener una pontencia usando una de las variables flotantes como base y la variable entera como potencia
"""

var_int1 = 30
var_int2 = 20
var_float1 = 25.5
var_float2 = 40.7
var_str1 = "Hola"
var_str2 = "15"
var_bool= True

suma_1 = var_int1 + int(var_str2)
suma_2 = var_int1 + var_int2 + int(var_str2) + var_float1
mod = var_int1 % var_int2
entero = var_int1 // var_int2
potencia = pow(var_float1, var_int1)

print(suma_1)
print(suma_2)
print(mod)
print(entero)
print(potencia)