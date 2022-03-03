def sumar(numero1,numero2):
    print('Se realizara la sumatoria ...')
    print(numero1+numero2)


sumar(5,7)

def nombre(x):
    '''Funcion que recibe un string y lo imprime por consola'''
    print(x)

nombre('Eduardo')

#mostrara la documentacion de la funcion si es que hay
print(nombre.__doc__)

usuario=[]
def registrar(nombre,email, telefono):
    '''aqui registraremos el usuario'''
    usuario.append({
        'nombre': nombre,
        'email':email,
        'telefono':telefono
    })

    return {
        'message':'Usuario registrado exitosamente',
        'usuario':usuario[0] 
         },True,1

#si una funcion retorna mas de un valor (retornara una tupla) entonces podemos hacer dos cosas:
#1. si solamente declaramos una variable ahi se almacenara toda la tupla, 2. si queremos
#almacenar cada valor de la tupla en una variable podemos hacer una destructuracion
#de esa tupla declarando el mismo numero de variables que el numero de contenidos d ela tupla
resultado,estado_civil, nacionalidad=registrar('Eduardo','ederiveroman@gmail.com','974207075')

print(resultado)
print(estado_civil)
print(nacionalidad)

productos=[]
#si nosotros creamos una funcion que opcional reciba ciertos parametros, estos parametros opcionales
#SIEMPRE deben de ir al final, primero los requeridos y luego los opcionales
def registrar_productos(nombre,precio,estado=True,almacen='Almacen del cercado'):
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'estado': estado,
        'almacen':almacen
    })
    return 'Producto agregado exitosamente'

#siempre tenemos que pasar obligatoriamente los parametros qe no tienen valores por defecto
registrar_productos('Tomates',4.50)
registrar_productos('Apio',1.40,False)
registrar_productos('Cebolla',5.30,True,'Almacen nuevo mercado')
#otra forma de pasar parametros
registrar_productos(almacen='Almacen de la costa', nombre='Pescado tilapia', precio=2.50)



#recibira un numero indeterminado de parametros y lo almacenera en una tupla
#puede recibir un numero indeterminado de parametros y estos pueden ser de diferentes tipos
def alumnos(clase,*args):
    print(args)
    #if(len(args) and args[0] is not None):
    #   print('Si hay el valor del puerto')
    print('la clase es:',clase)
#def alumnos(*args):
#   print(args)

alumnos('grupo12','eduardo','nahia','pedro','mario','jean carlo')

alumnos('frontend','eduardo','roxana','luis','joshua','danny')

alumnos('juanito')

alumnos('martha',30,False,'Juan',1.5)

#kwargs > keyword argument
#si la funcion queremos recibir un numero ilimitado de argumentos para estos deben de tener 
# su nomnre de parametro con su valor entonces usaremos los kwargs y estos se almacenaran
# en un diccionario
def ingresarProducto(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('El usuario quiere agregar un producto con el nombre')
    if(kwargs.get('cantidad')):
        print('El usuario quiere ingresar la cantidad del producto')

ingresarProducto(nombre='Manzana')





#Recursividad
# es utilizar la funcion dentro de la misma funcion

def saludar_n_veces(limite):
    if(limite==0):
        return 'Llegue al limite'
    print('saludar')
    return saludar_n_veces(limite-1)

resultado=saludar_n_veces(100)

print(resultado)


#5!

def factorial(limite):
    if limite == 0:
        return 1

    return limite * factorial(limite-1)

resultado = factorial(3)
print(resultado)       
# ventajas:
# * hace el codigo mas limpio y sin mucha duplicidad del mismo
# * una tarea compleja se puede dividir en si misma de una manera mas facil y sencilla
# * la generacion de subsecuencias es mas facil con la recursividad que con alguna iteracion anidada (while)

# desventajas:
# * a veces la logica para genera una funcion recursiva es dificil de seguir
# * las llamas recursivas son mas costosas ya que ocupan mas memoria por el simple echo de volver a llamar a toda la funcion de nuevo dentro de si misma y obviamente esto generara un mayor tiempo de respuesta
# * las funciones recursivas son dificiles de hace depuracion (seguimiento al codigo linea x linea)

#Operador ternarios






cuadrado= lambda numero: numero **2
sacar_igv=lambda precio: precio * 0.18

rpta=cuadrado(4)

precio_sin_igv = sacar_igv(100)
print(rpta)
print(precio_sin_igv)

precio_sin_igv = sacar_igv(50)
print(precio_sin_igv)