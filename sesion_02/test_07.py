"""Reconocimiento de tipo sde datos"""

"""Creacion de variables"""

nombre = "Luis"
ciudad = "Lima"
saldo =  5000
empresa = False
correo = "luis@gmail,com"
empleado = [nombre, saldo, empresa, ciudad]
empleado_d = {'nom' : nombre, 'sald' : saldo, 'ciud' : ciudad, 'corr' : correo, 'empre' : empresa}

print("Mi tipo de dato de la variables es: {}".format(type(nombre)))
print("Mi tipo de dato de la variables es: {}".format(type(ciudad)))
print("Mi tipo de dato de la variables es: {}".format(type(saldo)))
print("Mi tipo de dato de la variables es: {}".format(type(empresa)))
print("Mi tipo de dato de la variables es: {}".format(type(correo)))
print("Mi tipo de dato de la variables es: {}".format(type(empleado)))
print("Mi tipo de dato de la variables es: {}".format(type(empleado_d)))
