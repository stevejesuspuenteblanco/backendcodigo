# Esto es un comentario y sirve para dar contexto de que se hace se hizo o se hara
# TODO: logica para este controlador


edad = 30

# variables de texto

nombre = 'eduardo'
apellido= "de rivero"

#si queremos tener un texto que pueda contener saltos de line
descripcion = """hola amigos:

 como estan?
 yo muy bien jeje
 """

descripcion2 = '''hola amigos:

como estan?'''

desCripcion2="adios"


print(descripcion2)
print(desCripcion2)

#variables numericas
year=2022

#type() => mostrara que tipo de variable estan
print(type(year))
print(type(descripcion2))

#en python no se puede crear una variable sin ningun contenido
#a excepcion del none
#en python none = null | undefined
especialidad=None

#en python no hace validacion del tipo de dato primario (si 
# la variable 'nace' siendo string) normal se puede cambiar la
# su tipo a otro (Boolean, int, float, array, etc...)
# en python no existen las constantes
dni=[123123123]
dni='peruano'
dni=False

#id() > dara la ubicacion de esa variable en relacion  la memoria
# del dispositivo

print(id(dni))

print(type(especialidad))

mes, dia = "febrero",28

print(mes)

#elimina la variable de la memoria
del mes

print(mes)

