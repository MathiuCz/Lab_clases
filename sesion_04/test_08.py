"""
Requisitos
- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensualmenos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables usando asignación múltiple los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"
Hora máximo de envío: 8 pm

Correo a enviar solución: cerseuufisi@gmail.com
Asunto: participación 23 Mar - nombre apellido


"""
#Pidiendo los datos que solicita la empresa
var_1 = input("Ingrese su nombre: ")
var_2 = input("Ingrese su apellido paterno: ")
var_3 = input("Ingrese el distrito donode reside: ")
var_4 = int(input("Ingrese su sueldo: "))

#Bono final
bono_final = var_4*3 - 0.1*var_4

#Poniendo los datos en un diccionario
dic = {"nombre": var_1, "apellido paterno": var_2, "distrito": var_3, "bono final": bono_final}

#Asignando nuevas variables a mi lista
nombre = dic["nombre"]
apellido_paterno = dic["apellido paterno"]
distrito = dic["distrito"]
bono = dic["bono final"]

print("{} {}, recibirá {} soles de bono de fin de año".format(nombre, apellido_paterno, bono_final))