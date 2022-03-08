productId=input('Ingresa el id del producto: ')
try:
    if(productId == '10'):
        # emitira un erro manualmente
        # se utiliza para no continuar con el flujo normal del proyecto
        raise Exception('EL producto no existe en la bd')
    


except Exception as e: 
    print('Ups algo salio mal con el producto a buscar',e.args[0])
else:
    print('El producto encontrado es: ...')

print('Yo soy el final del programa')