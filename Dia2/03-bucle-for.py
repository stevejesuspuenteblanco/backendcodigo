notas = [10,20,16,8,6,1]

# for(let i=0; i<10, i++){...}
# en cada iteracion tendremos su valor y lo almacenaremos en una variable llamada notas
#el mismo funcionamiento se da para cualquier coleccion de datos

for nota in notas:
    print(nota)

#crearemos un bucle manual para una iteracion con limite 10
for numero in range(10):
    print(numero)

#con dos parametros el primero es donde inicia y el segundo donde termina
for numero in range(5,10):    
    print(numero)


#si colocamos dos parametros el primeri es numero inicial, el segundo el que termina y 
#el tercero en cuanto hara la decrementacion
for numero in range(5,10,2):
    print(numero)

#imprimir los tres valores iniciales de notas

aprobados=['Pedro','Eduardo','Maria','Fatima']

for aprobado in aprobados:
    if(aprobado == 'Pedro'):
        print('Pedro esta aprobado')
        break
    print('El aprobado es:',aprobado)
else: 
    print('Termino ejecutarse el for de manera normal')
#else se ejecutara siempre que termine el bucle
print('Termino de ejecutarse el for')


productos=['Manzanas','Peras','Tallarines','Tazas']

busqueda = input('Ingrese el producto a buscar:')

for producto in productos:
    if producto == busqueda:
        print('El producto si esta en la tienda')
        break
else:
    print('No se encontro el producto')   

print('Igual yo me ejecuto') 