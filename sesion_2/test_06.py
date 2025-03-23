"""
Requisitos

1. Crear variables para los valores de nombre, profesion y ciudad
2. Crear 2 variables de remuneracion de enero y febrero (+ de 1000)
3. crear una variables donde se sumara el ingreso de los meses de enero y febrero
4. Mostrar en pantalla el mensaje de:

"Hola soy (nombre) mi profesion es (profesion) y mi remuneracion acumulada es de (remuneracion total)"

"""

nombre = "Mathius"
profesion = "fisico"
ciudad =  "Lima"

re_enero = 3400
re_febrero = 1200

suma_total = re_enero + re_febrero

print("Hola soy {} mi profesion es {} y mi remuneracion acumulada es de {}".format(nombre, profesion, suma_total))