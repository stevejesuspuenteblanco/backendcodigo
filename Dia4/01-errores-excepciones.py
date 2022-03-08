# un error es una mala ejecucion del codigo 
# que hara que el script deje de funcionar

#en python se tiene varias alertas para los sucesos

#locals()['__builtins'] > me retornara del diccionario
#de locals todos los errores definidos dentro de python y los
#atributos de los errores.
#dir > nos permite listar estos atributos
#print(dir(locals()['__builtins__']))   >listamos errores

#todo try tiene que tener OBLIGATORIAMENTE un except
try:
    valor=int(input('Ingresa un numero: '))
    print(valor)
except ValueError:
    #entrara a este except cuando el error sea de tipo
    #typeerror
    print('Error ala convertir un strin a un numero')
except Exception as error:
    print(error.args)
    #Capturara el error causante impididiendo que el
    #programa deje de funcionar
    #solamente ingresara cuando tengamos un error
    print('Oops algo salio mal intentalo denuevo')
print('Yo finalizo correctamente')

while True:
    try:
        valor=int(input('Ingresa un numero: '))
        break
    except:
        print('Valor incorrecto, solo pueden ser numeros')
print(valor)   

try:
    resultado=1/1
    #voy a buscar el producto a la base de datos
    producto=None
    if (producto is None):
        raise Exception('El producto no existe en la bd')
except:
    print('hubo un error')
else:
    print('Yo soy el else')
finally:
    print('Yo me ejecutare si todo fue bien y fue mal')