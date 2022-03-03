#mientras que
#numero=0
#while numero<10:
    #pass sirve para indicar dentro de un bloque de codigo que no hemos definido la logica
    #que no hague nada pero que no de error 
#    print(numero)
    #bucle infinito
#    numero+=1
#else: 
#    print('EL while termino bien')



numeros=[1,5,16,28,234,67,29]
#hay x numeros pares
#hay y numeros impares
par, impar = 0,0
for numero in numeros:
    if numero % 2 ==0:
        par+=1
    else:
        impar+=1    

print('Hay {} numeros pares'.format(par))
print('Hay {} numeros impares'.format(impar))

# AHORA CON WHILE

posicion=0
par, impar=0,0

while posicion< len(numeros):
    if numeros[posicion] % 2== 0:
        par+=1
    else:
        impar+=1
    posicion+=1

print('Hay {} numeros pares'.format(par))
print('Hay {} numeros impares'.format(impar))    